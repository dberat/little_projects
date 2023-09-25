import random


def score(p1, p2):

    print("TOTAL SCORE".center(31, "-"))
    print(f"Player 1:  {p1}".rjust(18, "-"))
    print(f"Player 2:  {p2}".rjust(18, "-"))


def game_cvsc():
    print("Welcome to Automated Rock-Paper-Scissors...")
    user = int(input("Please enter how many round automated players should play the game: "))
    options = ["r", "p", "s"]
    score_p1 = 0
    score_p2 = 0
    count = 0

    while count < user:

        player_1 = random.choice(options)
        player_2 = random.choice(options)

        if player_1 == "r" and player_2 == "r":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("TIE")
        elif player_1 == "p" and player_2 == "p":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("TIE")
        elif player_1 == "s" and player_2 == "s":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("TIE")
        elif player_1 == "r" and player_2 == "p":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("***PLAYER 2 WINS THIS ROUND***")
            score_p2 += 1
        elif player_1 == "r" and player_2 == "s":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("***PLAYER 1 WINS THIS ROUND***")
            score_p1 += 1
        elif player_1 == "s" and player_2 == "r":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("***PLAYER 2 WINS THIS ROUND***")
            score_p2 += 1
        elif player_1 == "s" and player_2 == "p":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("***PLAYER 1 WINS THIS ROUND***")
            score_p1 += 1
        elif player_1 == "p" and player_2 == "r":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("***PLAYER 1 WINS THIS ROUND***")
            score_p1 += 1
        elif player_1 == "p" and player_2 == "s":
            print(f"Player 1 has chosen: {player_1}\nPlayer 2 has chosen: {player_2}")
            print("***PLAYER 2 WINS THIS ROUND***")
            score_p2 += 1
        count += 1

    if score_p1 < score_p2:
        score(score_p1, score_p2)
        print("PLAYER 2 WON THE GAME".center(41, "*"))
    elif score_p1 == score_p2:
        score(score_p1, score_p2)
        print("TIE".center(23, "*"))
    else:
        score(score_p1, score_p2)
        print("PLAYER 1 WON THE GAME".center(39, "*"))
