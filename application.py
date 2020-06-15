import os
import requests
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
from collections import deque
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.secret_key = 'asr'

d = {}

@app.route("/")
def index():
    if 'name' in session:
        if session.get('currentChannel') is None:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('channel', channel=session.get('currentChannel')))
    else:
        return render_template("index.html")

@app.route("/home", methods=["POST", "GET"])
def home():
    session['currentChannel'] = None
    if session.get("success") is None:
        session['success'] = True;

    if request.method == "GET":
        if 'name' in session:
            return render_template("home.html", name=session['name'], channels=session['channels'], success=session['success'])
    else:
        session['name'] = request.form.get("name")
        return render_template("home.html", name=session['name'], channels=session['channels'])

@app.route("/logout")
def logout():
    session.pop('name')
    return redirect(url_for('index'))

@app.route("/addChannel", methods=["POST"])
def addChannel():
    channelName = request.form.get("fname")

    if session.get("channels") is None:
        session["channels"] = []

    session['success'] = True
    channels = session['channels']

    if channelName in session['channels']:
        session['success'] = False

    elif channelName != "" and channelName not in channels:
        channels.append(channelName)
        session['channels'] = channels

    return redirect(url_for('home'))

@app.route("/channel/<string:channel>", methods=["GET", "POST"])
def channel(channel):

    session['currentChannel'] = channel

    messages = d.get(channel, [])

    return render_template('channel.html', channel=channel, messages=messages)

@socketio.on("submit message")
def message(data):
    channel = session['currentChannel']
    message = data['message']
    time = datetime.datetime.now().strftime("%x-%X")

    if channel not in d.keys():
        d[channel] = deque([{'message': message, 'author': session['name'], 'time': time}], 100)
    else:
        d[channel].append({'message': message, 'author': session['name'], 'time': time})

    emit("announce message", {'message': message, 'author': session['name'], 'time': time}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
