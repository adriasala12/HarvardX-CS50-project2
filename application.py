import os

from flask import Flask, render_template, request, session, redirect, url_for
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
    if request.method == "GET":
        if 'name' in session:
            if 'channels' in session:
                return render_template("home.html", name=session['name'], channels=session['channels'])
            else:
                return render_template("home.html", name=session['name'])
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
    print(channelName)

    return redirect(url_for('home'))
