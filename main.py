from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import json
from collections import defaultdict

games = []
gameCounter = 0
players = []
playerCounter = 0
gameSockets: dict[int: list[WebSocket]] = defaultdict(list)
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
        "openToConnection": True,
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


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str, game: dict):
        for connection in gameSockets[game["gameId"]]:
            await connection.send_text(json.dumps(message))

manager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
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
                gameSockets[gameCounter].append(websocket)
                await websocket.send_text(json.dumps(game))


            
            if (method == "update"):
                #frontend sends update event ... now we need to recognize for which game the update is meant to be so we can only update board for the respective players
                print("updatingggg.....")
                print(gameSockets)
                payLoad = {
                    "method" : "update",
                    "cells" : message["cells"]
                } 
                await manager.broadcast(payLoad, game)
                await websocket.send_text(json.dumps(payLoad))
            
    except WebSocketDisconnect:
        pass

