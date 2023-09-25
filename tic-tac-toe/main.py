board = {"7": " ", "8": " ", "9": " ",
         "4": " ", "5": " ", "6": " ",
         "1": " ", "2": " ", "3": " "}

print("Welcome to TIC-TAC-TOE...")


def print_board():
    print(f'{board["7"]} | {board["8"]}| {board["9"]}')
    print("--+--+--")
    print(f'{board["4"]} | {board["5"]}| {board["6"]}')
    print("--+--+--")
    print(f'{board["1"]} | {board["2"]}| {board["3"]}')


def game():

    turn = "X"
    count = 0

    for i in range(10):
        print_board()
        move = input(f"It's your turn {turn}. Select a box to mark.")

        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("That box is already marked. Please select another box.")
            continue

        if count >= 5:
            if board["1"] == board["2"] == board["3"]:
                print_board()
                print(f"Game over. {turn} has won.")
                break

            elif board["1"] == board["4"] == board["7"]:
                print_board()
                print(f"Game over. {turn} has won.")
                break

            elif board["1"] == board["5"] == board["9"]:
                print_board()
                print(f"Game over. {turn} has won.")
                break

            elif board["4"] == board["5"] == board["6"]:
                print_board()
                print(f"Game over. {turn} has won.")
                break

            elif board["7"] == board["8"] == board["9"]:
                print_board()
                print(f"Game over. {turn} has won.")
                break

            elif board["2"] == board["5"] == board["8"]:
                print_board()
                print(f"Game over. {turn} has won.")
                break

            elif board["3"] == board["6"] == board["9"]:
                print_board()
                print(f"Game over. {turn} has won.")
                break

            elif board["7"] == board["5"] == board["3"]:
                print_board()
                print(f"Game over. {turn} has won.")
                break

        if count == 9:
            print("---TIE---")
            break
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart = input("Would you like to play again?(y/n): ").lower
    if restart == "y":
        for key in board.keys():
            board[key] = " "
        game()
    else:
        print("Have a good one!")
        

game()
