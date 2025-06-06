from enum import Enum

class RandomClass(str, Enum):
    pass

a = RandomClass
print(type(a))