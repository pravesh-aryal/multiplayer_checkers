from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_socketio import SocketIO
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = "some_secret_key"
socketio = SocketIO(app)


def initdb():

    #database
    conn = 0
    if not conn:
        conn = psycopg2.connect(database="flask_db", user="postgres", password="root", host="127.0.0.1", port="5432")

        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                password VARCHAR(100)
            );
        ''')
    return conn, cur



@app.route("/home", methods = ['GET', 'POST'])
def home():
    # conn = initdb()
    return render_template("home.html")

@app.route("/login", methods = ['POST'])
def login():
    conn = initdb()
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # user = get_user_from_db(username)  # Your DB lookup here
    user = 'test'
    if  user != username:
        
        return jsonify({"success": False, "message": "Invalid username or password"}), 401

    # session login here, or return auth token
    # return redirect(url_for(test))
    return jsonify({"success": True, "message": "Login successful"})
    
@app.route("/player_options", methods= ['GET', 'POST'])
def player_options():
    return render_template("player_options.html")


@app.route("/signup", methods = ['POST'])
def signup():
    (conn, cur) = initdb()
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    #maintain some array and create a user for that username
    ####
    print("USERNAME IS: ", username)
    print("DOP I GET HERE")

    cur.execute("SELECT 1 FROM players WHERE name = %s;", (username,))
    exists = cur.fetchone() is not None

    if exists:
        print("Username already exists.")
        return jsonify({"message": "Player already exists try different username" })
    else:
        cur.execute(
            "INSERT INTO players (name, password) VALUES (%s, %s);",
            (username, password)
        )    
        conn.commit()
        print("Username is available.")
        return jsonify({"message": "Account creation succesful."})


@socketio.on('my event')
def handle_message(message):
    print("RECEIVED", message)

if __name__ == "__main__":
    socketio.run(app)



