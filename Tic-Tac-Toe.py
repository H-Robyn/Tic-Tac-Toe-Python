import random


# Example Board
def example_board():
    print()
    print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
    print('---|---|---')
    print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
    print('---|---|---')
    print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
    

# Print Tic-Tac-Toe Board
def print_board(marker, player=' ', position=0):
    marker[position] = player
    print()
    print(' ' + marker[1] + ' | ' + marker[2] + ' | ' + marker[3])
    print('---|---|---')
    print(' ' + marker[4] + ' | ' + marker[5] + ' | ' + marker[6])
    print('---|---|---')
    print(' ' + marker[7] + ' | ' + marker[8] + ' | ' + marker[9])


# Player Choose [ X | O ]
def player_choose():
    player = ''
    while not (player == 'X' or player == 'O'):
        player = input("Enter Player [X | O]: ").upper()

    if player == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Winner Check
def check_winner(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker))


# Choose First and Toggle Players
def choose_toggle_player():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# Choose First Turn and Toggle Computer Player
def choose_toggle_computerplayer():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Computer'


# Check Available Space in Board
def space_check(board, position):
    return board[position] == ' '


# Check if the Board is Full
def full_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Player Choose the Position to put marker [ X | O ] -> For Player VS Player
def player_choose_position(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Enter The Position: "))
    return position


# Computer Choose the Position to put marker [ X | O ] -> For Computer VS Player
def computer_choose_position(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = random.randint(1, 9)
    return position


# To Replay the Game
def replay():
    return input("Do you want to Play Again? Press [ Yes | No]: ").lower().startswith('y')


# Driver-Code
def main_runner():
    # Player VS Player
    def between_players():
        while True:
            ttt_board = [' '] * 10
            player1_marker, player2_marker = player_choose()
            turn = choose_toggle_player()
            print(turn + ' is First To Move')
            play_game = input("Are you Ready? Press [Y | N]: ").upper()

            if play_game == 'Y':
                game_on = True
            else:
                game_on = False

            while game_on:
                if turn == 'Player 1':
                    pos = player_choose_position(ttt_board)
                    print_board(ttt_board, player1_marker, pos)

                    if check_winner(ttt_board, player1_marker):
                        print_board(ttt_board)
                        print(turn + ' You Win!')
                        game_on = False
                    else:
                        if full_check(ttt_board):
                            print('Game Tie')
                            break
                        else:
                            turn = 'Player 2'
                else:
                    pos = player_choose_position(ttt_board)
                    print_board(ttt_board, player2_marker, pos)

                    if check_winner(ttt_board, player2_marker):
                        print(turn + ' You Win!')
                        game_on = False

                    else:
                        if full_check(ttt_board):
                            print('Game Tie')
                            break
                        else:
                            turn = 'Player 1'
            if not replay():
                break

    # Player VS Computer
    def between_computerplayer():
        while True:
            ttt_board = [' '] * 10
            player1_marker, player2_marker = player_choose()
            turn = choose_toggle_computerplayer()
            print(turn + ' is First To Move')
            play_game = input("Are you Ready? Press [Y | N]: ").upper()

            if play_game == 'Y':
                game_on = True
            else:
                game_on = False

            while game_on:
                if turn == 'Player 1':
                    pos = player_choose_position(ttt_board)
                    print_board(ttt_board, player1_marker, pos)

                    if check_winner(ttt_board, player1_marker):
                        print(turn + ' You Win!')
                        game_on = False
                    else:
                        if full_check(ttt_board):
                            print('Game Tie')
                            break
                        else:
                            turn = 'Computer'

                else:
                    pos = computer_choose_position(ttt_board)
                    print_board(ttt_board, player2_marker, pos)

                    if check_winner(ttt_board, player2_marker):
                        print(turn + ' Win!')
                        game_on = False

                    else:
                        if full_check(ttt_board):
                            print('Game Tie')
                            break
                        else:
                            turn = 'Player 1'
            if not replay():
                break

    print("Welcome to Tic-Tac-Toe", end='\n')
    print()
    example_board()
    print()
    print("Choose Mode")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    choose_mode = int(input("Press 1 or 2: "))
    if choose_mode == 1:
        between_players()
    else:
        between_computerplayer()


# Invoke-Driver-Code
main_runner()
