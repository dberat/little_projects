
def if_valid_chess_board(board):
    count = 0
    black = 0
    white = 0
    bpawn = 0
    wpawn = 0
    location = ["a","b","c","d","e","f","g","h"]
    if "bking" not in board.values() or "wking" not in board.values():
        print("There must be both black and white king.")
        return False
    for v in board.values():
        count += 1


        if v.startswith("b"):
            black += 1

        elif v.startswith("w"):
            white += 1

        elif black > 16 or white > 16:
            print("A player can posses at most 16 pieces.")
            return False

    for v in board.values():
        if v.startswith("bp"):
            bpawn += 1

        elif v.startswith("wp"):
            wpawn += 1

            if bpawn > 8 or wpawn > 8:
                print("A player can posses at most 8 pieces pawns.")
                return False

    for k in board.keys():
        for c in k:
            if int(k[0]) > 8:
                print("Location's first character can not be greater than 8")
                return False

            elif not k[1] in location:
                print("Location's second character can only be between a-h")
                return False

    if True:
        return True


the_board = {"1h": "bking", "3c": "wpawn", "2g": "bbishop",
             "5h": "bqueen", "3e": "wking","4h": "wpawn",
             "4d": "wpawn","5b": "wpawn","6b": "wpawn",
             "4b": "wpawn","5d": "wpawn","6d": "wpawn",
             "4c": "wpawn","5c": "wpawn","6c": "wpawn"}

print(if_valid_chess_board(the_board))
