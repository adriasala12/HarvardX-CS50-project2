import os

from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
#from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#Session(app)
app.secret_key = 'asr'
#session['name'] = None

@app.route("/")
def index():
    if 'name' in session:
        return render_template("home.html", name=session['name'])
    else:
        return render_template("index.html")

@app.route("/home", methods=["POST"])
def home():
    session['name'] = request.form.get("name")
    return render_template("home.html", name=session['name'])
