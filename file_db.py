import csv
playersFile = "players.csv"
gamesFile = "games.csv"

games = []


def getPlayerList():
    players: list = []
    with open(playersFile, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            players.append(row)
    return players

def getPlayerFromId(playerId: int):
    pass

def playerAlreadyExists(username: str) -> bool:
    playersList: list = getPlayerList()
    for playerEntry in playersList:
        if playerEntry[1] == username:
            print(playerEntry[1], username)
            return True
        
    return False


def storeNewPlayer(userid: str, username: str, password: str):
    with open(playersFile, "a", newline="\n") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([userid, username, password])

def isCorrectPassword(username: str, password: str):

    return True
