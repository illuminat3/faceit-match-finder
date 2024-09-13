from faceitapi import *

if __name__ == "__main__":
    username = ""
    userId = ExtractAccountId(username)
    matchCount = ExtractMatchCount(userId)
    does_game_exist = IsGameFound(userId, matchCount)

    if does_game_exist:
        print("Match Found")