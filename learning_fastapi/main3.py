# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/players/{player_id}/games/{game_id}")
# async def read_player_name(
#     player_id: int,
#     game_id: str,
#     q: str,
#     short: bool = False
# ):
#     game = {"game_id": game_id, "owner_id": player_id}
#     if q:
#         game.update({"q": q})
    
#     if not short:
#         game.update(
#             {
#                 "description": "Game with a description"
#             }
#         )
#     return game


from fastapi import FastAPI
from pydantic import BaseModel

class Player(BaseModel):
    username: str
    about: str | None = None
    ratio: float
    points: float | None = None

app = FastAPI()

@app.post("/players/")
async def create_player(player: Player):
    player_dict = player.model_dump()
    if player.points is not None:
        player_total_points = player.ratio + player.points
        player_dict.update(
            {
                "final_points": player_total_points
            }
        )
    print(player_dict)
    return player_dict