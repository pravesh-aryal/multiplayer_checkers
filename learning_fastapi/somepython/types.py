# def get_full_name(first_name: str, last_name: str):
#     return first_name.title() + " " + last_name.title()


# print(get_full_name("pravesh", "aryal"))


# items: list[str, int] = [1, 2, 3, 'pravesh', 'winne', 'the pooh']
# print(items)


# from typing import Optional


# def say_hi(name: Optional[str] = None):
#     if name is not None:
#         print(f"Hey {name}!")
#     else:
#         print("Hello World")

# say_hi()



from datetime import datetime
from pydantic import BaseModel
from typing import NewType, Annotated

class Player(BaseModel):
    uid: int
    username: str = "player x"
    login_ts: datetime | None = None
    added_friends: list[int] = []

player1_data = {
    "uid": 1,
    "login_ts": "2017-06-01 12:22",
    "added_friends": [2, 3, 4],
}

player = Player(**player1_data)
print(player)
print(player.uid)


def greet(name: Annotated[str, "This is person name metadata"]) -> str:
    print(f"Hello {name}")

greet("Winnie")
