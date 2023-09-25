import random


def score(p, c):

    print("TOTAL SCORE".center(31, "-"))
    print(f"Player:{p}".rjust(12, "-"))
    print(f"Computer:{c}".rjust(14, "-"))


def game_pvsc():
    print("Welcome to Rock-Paper-Scissors...")
    print("r --> Rock\np --> Paper\ns --> Scissors")
    options = ["r", "p", "s"]
    score_p = 0
    score_c = 0

    while True:

        player = input("Please choose your move (r/p/s)(e for exit): ").lower()
        computer = random.choice(options)
        if player not in ["r", "p", "s", "e"]:
            print("Please choose a valid option(r/p/s/e)...")
            continue
        if player == "r" and computer == "r":
            print(f"Computer has chosen: {computer}")
            print("TIE")
        elif player == "p" and computer == "p":
            print(f"Computer has chosen: {computer}")
            print("TIE")
        elif player == "s" and computer == "s":
            print(f"Computer has chosen: {computer}")
            print("TIE")
        elif player == "r" and computer == "p":
            print(f"Computer has chosen: {computer}")
            print("***COMPUTER WINS THIS ROUND***")
            score_c += 1
        elif player == "r" and computer == "s":
            print(f"Computer has chosen: {computer}")
            print("***PLAYER WINS THIS ROUND***")
            score_p += 1
        elif player == "s" and computer == "r":
            print(f"Computer has chosen: {computer}")
            print("***COMPUTER WINS THIS ROUND***")
            score_c += 1
        elif player == "s" and computer == "p":
            print(f"Computer has chosen: {computer}")
            print("***PLAYER WINS THIS ROUND***")
            score_p += 1
        elif player == "p" and computer == "r":
            print(f"Computer has chosen: {computer}")
            print("***PLAYER WINS THIS ROUND***")
            score_p += 1
        elif player == "p" and computer == "s":
            print(f"Computer has chosen: {computer}")
            print("***COMPUTER WINS THIS ROUND***")
            score_c += 1
        elif player == "e":
            break

    if score_p < score_c:
        score(score_p, score_c)
        print("COMPUTER WON THE GAME".center(41, "*"))
    elif score_p == score_c:
        score(score_p, score_c)
        print("TIE".center(23, "*"))
    else:
        score(score_p, score_c)
        print("PLAYER WON THE GAME".center(39, "*"))
