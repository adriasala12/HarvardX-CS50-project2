import os

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.secret_key = 'asr'

@app.route("/")
def index():
    if 'name' in session:
        return redirect(url_for('home'))
    else:
        return render_template("index.html")

@app.route("/home", methods=["POST", "GET"])
def home():

    if session.get("success") is None:
        session['success'] = True;

    if request.method == "GET":
        if 'name' in session:
            return render_template("home.html", name=session['name'], channels=session['channels'], success=session['success'])
    else:
        session['name'] = request.form.get("name")
        return render_template("home.html", name=session['name'])

@app.route("/logout")
def logout():
    session.clear()
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
        # if request.method == "POST":
        channels.append(channelName)
        session['channels'] = channels

    return redirect(url_for('home'))


@app.route("/channel/<string:name>")
def channel(name):
    if session.get('{name}') is None:
        session['{name}'] = ['test message']

    print(session['{name}'])
    return render_template('channel.html', name=name)
