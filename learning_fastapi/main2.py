# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message" : "HELLO WORLD"}

# @app.get("/player/me")
# async def read_player_me():
#     return {
#         "player_id" : "the current player"
#     }

# @app.get("/player/{player_id}")
# async def read_player(player_id: int):
#     return {"player_id" : player_id}


# from enum import Enum

# from fastapi import FastAPI

# class AIModelName(str, Enum):
#     perceptron = "perceptron"
#     gpt = "gpt"
#     regression = "regression"

# app = FastAPI()

# @app.get("/models/{model_name}")
# async def get_model_name(model_name: AIModelName):
#     whattype = str(type(model_name))
#     if model_name is AIModelName.perceptron:
#         return {
#             "model_name" : model_name,
#             "message" : "Perceptron model ",
#             "type" : whattype,
#         }
#     if model_name.value == "gpt":
#         return {
#             "model_name": model_name,
#             "message": "I am GPT",
#             "type" : whattype,

#         }
#     return{
#         "model_name": model_name,
#         "message" : "Regression ..???",
#         "type" : whattype,
#     }


from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}