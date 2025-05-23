from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_socketio import SocketIO
import psycopg2
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "some_secret_key"
socketio = SocketIO(app)

board_config = []
#just for validation purpose to make succesful move is transfered and commited to db and board is synced in between users. 
def move_is_succesful():
    board_config.append("succesful")
    (conn, cur) = initdb()
    cur.execute("""
    UPDATE games
    SET board_config = %s
    WHERE id = %s;
""", (json.dumps(board_config), 1))





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
        
        cur.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id SERIAL PRIMARY KEY,
            board_config JSONB
        );
                    
    ''')
        cur.execute(
"INSERT INTO games (board_config) VALUES (%s);",
(json.dumps(board_config),)
)
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
    user = ['user', 'user2']
    if  username not in user:
        
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


@app.route("/game/pvp")
def play():
    move_is_succesful()
    return render_template("checkers.html", board_config=board_config)

@socketio.on('my event')
def handle_message(message):
    print("RECEIVED", message)

@socketio.on('player_move')
def handle_player_move(data):
    move_is_succesful()
    conn, cur = initdb()
    cur.execute("SELECT board_config FROM games WHERE id = %s;", (1,))
    board = cur.fetchone()[0]  # JSONB is returned as Python list

    cur.execute(
        "UPDATE games SET board_config = %s WHERE id = %s;",
        (json.dumps(board), 1)
    )
    conn.commit()
    cur.close()
    print("DO I COMHEREIORHdiafshslkdfhlakshf")
    # Send updated board back to all players in this game
    socketio.emit("board_update", {"board_config": board_config})


if __name__ == "__main__":
    socketio.run(app)



