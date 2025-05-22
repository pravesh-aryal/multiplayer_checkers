from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "some_secret_key"
socketio = SocketIO(app)

@app.route("/home", methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/login", methods = ['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if (username == 'testuser' and password == 'password'):
        return jsonify({"message": "login successful"})
    else:
        return jsonify({"message": "invalid credentials"}), 401
    

@socketio.on('my event')
def handle_message(message):
    print("RECEIVED", message)

if __name__ == "__main__":
    socketio.run(app)



