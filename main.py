from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import json

games = []
gameCounter = 0
players = []
playerCounter = 0

app = FastAPI()

def getFirstOpenGame():
    if not games:
        return games
    
    for game in games:
        if (game["openToConnection"]):
            game["openToConnection"] = False
            return game

def createGame():
    global gameCounter
    gameCounter += 1
    game = {
        "gameId": gameCounter,
        "players": [],
        "openToConnection": True
    }
    games.append(game)
    return game

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/home.html")

@app.get("/signup")
def signup():
    return FileResponse("static/signup.html")


@app.get("/login")
def login():
    return FileResponse("static/login.html")

@app.get("/gamescreen")
def gamescreen():
    return FileResponse("static/gamescreen.html")



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            message = json.loads(data)
            method = message.get("method")

            if (method == "join"):
                global playerCounter
                playerCounter += 1
                playerId = playerCounter
                # get the first open game if any
                game = getFirstOpenGame()
                if not game:
                    game = createGame()
                #now connect to that game
                game["players"].append(playerId)
                print(games)
            
    except WebSocketDisconnect:
        pass
        