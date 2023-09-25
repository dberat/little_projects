from PvsC import game_pvsc
from CvsC import game_cvsc
from PvsP import game_pvsp

while True:
    user = input("""Welcome to Berat's Rock-Paper-Scissors Game
If you want to play against your friend Press 1
If you want to play against computer Press 2
If you want computer to play it for you Press 3
(e for exit): """).lower()
    if user == "1":
        game_pvsp()
    elif user == "2":
        game_pvsc()
    elif user == "3":
        game_cvsc()
    elif user == "e":
        break
