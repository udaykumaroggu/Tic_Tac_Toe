board = [' ' for _ in range(9)]
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')
def check_winner():   
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True   
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True   
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    return False
def play_game():
    print("Let's play Tic-Tac-Toe!")
    print_board()
    while True:
        user_move = int(input("Enter your move (1-9): ")) - 1
        if board[user_move] == ' ':
            board[user_move] = 'X'
        else:
            print("Invalid move. Try again.")
            continue
        print_board()
        if check_winner():
            print("Congratulations! You win!")
            break
        if ' ' not in board:
            print("It's a tie!")
            break
        system_move = None
        for i in range(9):
            if board[i] == ' ':
                system_move = i
                break
        board[system_move] = 'O'
        print("System's move:")
        print_board()
        if check_winner():
            print("Sorry, you lose!")
            break
play_game()
