from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "some_secret_key"
socketio = SocketIO(app)

@app.route("/home", methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@socketio.on('my event')
def handle_message(message):
    print("RECEIVED", message)

if __name__ == "__main__":
    socketio.run(app)



