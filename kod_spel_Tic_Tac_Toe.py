print("#################")
print("### TRE I RAD ###")
print("#################")

# Spelbrädet
board = [["-" for _ in range(3)] for _ in range(3)]

# Skriv ut spelbrädet
def print_board():
    for row in board:
        print(" | ".join(row))
    print()

# Kolla om någon har vunnit
def has_winner():
    # Kolla rader
    for row in board:
        if row[0] == row[1] == row[2] != "-":
            return True
    # Kolla kolumner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return True
    # Kolla diagonaler
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True
    return False

# Kolla om det är oavgjort
def is_tie():
    for row in board:
        if "-" in row:
            return False
    return True

# Byt spelare
def switch_player(player_turn):
    return "O" if player_turn == "X" else "X"

# Starta spelet
def play(player_turn):
    while True:
        print_board()
        print("Spelare " + player_turn + ", din tur.")

        input_ok = False
        while not input_ok:
            rad = input("Välj rad (1-3): ")
            kolumn = input("Välj kolumn (1-3): ")

            if rad in ["1", "2", "3"] and kolumn in ["1", "2", "3"]:
                rad = int(rad) - 1  # Justera för listaindex
                kolumn = int(kolumn) - 1  # Justera för listaindex
                if board[rad][kolumn] == "-":
                    input_ok = True
                else:
                    print("Platsen är upptagen. Försök igen.")
            else:
                print("Felaktig inmatning. Försök igen.")

        # Placera markören
        board[rad][kolumn] = player_turn

        # Kolla om någon har vunnit eller om det är oavgjort
        if has_winner():
            print_board()
            print("Spelare " + player_turn + " vann!")
            break
        elif is_tie():
            print_board()
            print("Spelet blev oavgjort.")
            break

        # Byt spelare
        player_turn = switch_player(player_turn)

play("X")
