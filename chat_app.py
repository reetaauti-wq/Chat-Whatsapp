from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, join_room, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session['room'] = request.form['room']
        return redirect(url_for("chat"))
    return render_template("index.html")

@app.route("/chat")
def chat():
    if "room" not in session:
        return redirect(url_for("index"))
    return render_template("chat.html", room=session["room"])

@socketio.on("join")
def on_join(data):
    username = data["username"]
    room = session.get("room")
    join_room(room)
    send(f"{username} has entered the room {room}.", to=room)

@socketio.on("message")
def handle_message(data):
    room = session.get("room")
    send(data["msg"], to=room)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
