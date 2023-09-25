import getpass


def score(p1, p2):

    print("TOTAL SCORE".center(31, "-"))
    print(f"Player 1:  {p1}".rjust(18, "-"))
    print(f"Player 2:  {p2}".rjust(18, "-"))


def game_pvsp():
    print("Welcome to Rock-Paper-Scissors...")
    print("r --> Rock\np --> Paper\ns --> Scissors")
    print("If you do not choose one of those above, other player will earn 1 point!!!")
    user = int(input("Please enter how many round would you like to play?"))
    score_p1 = 0
    score_p2 = 0
    count = 0
    while count < user:

        player_1 = getpass.getpass("Player 1, please choose your move (r/p/s): ")
        player_2 = getpass.getpass("Player 2, please choose your move (r/p/s): ")

        if player_1 not in ["r", "p", "s"]:
            print("Player 1, please choose a valid option next time(r/p/s)...")
            print("Since Player 1 did not choose a valid option Player 2 has earned 1 point")
            score_p2 += 1
        elif player_2 not in ["r", "p", "s"]:
            print("Player 2, please choose a valid option next time(r/p/s)...")
            print("Since Player 2 did not choose a valid option Player 1 has earned 1 point")
            score_p1 += 1
        elif player_1 == "r" and player_2 == "r":
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
