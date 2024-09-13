from faceitapi import *

if __name__ == "__main__":
    username = "ErdNuckll"
    userId = extractAccountId(username)
    matchCount = extractMatchCount(userId)
    does_game_exist = isGameFound(userId, matchCount)

    if does_game_exist:
        print("Match Found")