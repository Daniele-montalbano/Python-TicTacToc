#!/usr/bin/env python
# coding: utf-8

# In[8]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print(' ' + board[7]+ ' ' + '|' + ' ' + board[8] + ' ' + '|'+ ' ' + board[9] + ' ')
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print('-'*11)
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print(' ' + board[4]+ ' ' + '|' + ' ' + board[5] + ' ' + '|'+ ' ' + board[6] + ' ')
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print('-'*11)
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print(' ' + board[1]+ ' ' + '|' + ' ' + board[2] + ' ' + '|'+ ' ' + board[3] + ' ')
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)

    
def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 Marker)
    '''
    player1 = input('Player1: Do you want to be X or O\t').upper()
    while player1 not in ('X','O'):
            print('The value is not allowed, please insert only "X" or "O"')
            player1 = input('Player1: Do you want to be X or O\t').upper()
        
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print('Player 1 is {}'.format(player1))
    print('Player 2 is {}'.format(player2))
    
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) or
            (board[7]==mark and board[8]==mark and board[9]==mark) or
            (board[1]==mark and board[5]==mark and board[9]==mark) or
            (board[3]==mark and board[5]==mark and board[7]==mark) or
            (board[1]==mark and board[4]==mark and board[7]==mark) or
            (board[2]==mark and board[5]==mark and board[8]==mark) or
            (board[3]==mark and board[6]==mark and board[9]==mark))


import random
def choose_first():
    if random.randint(1,2) == 1: 
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return (board[position]) == ' '
    
    
def full_board_check(board):
    return ' ' not in board
    

def player_choice(board):
    next_position = int(input('Choose your next position (1-9)\n'))
    
    while next_position not in range(1,10) or not space_check(board, next_position):
        print('The value is not allowed, please insert only number between 1 and 9')
        next_position = int(input('Choose your next position (1-9)\n'))
    
    return next_position
    

def replay():
    answer = input('Do you want to play again? Enter Yes or No:\t').upper()
    while answer not in ('YES','NO','Y','N'):
        print('The value is not allowed, please insert only "Yes" or "No":')
        answer = input('Do you want to play again? Enter Yes or No:\t').upper()
    if answer in ('YES','Y') : return True
    else: print('\nExit the game')

    

def TicTacToe():
    print('Welcome to Tic Tac Toe!')
    #print('\nHere you can see the board and the position of each cell')
    #display_board([0,'1','2','3','4','5','6','7','8','9'])
    #print('\n')
    
    #WHILE LOOP to keep running the game
    while True:
        board = ['#']+[' ']*9
        
        print('\n')
        player1, player2 = player_input() #to assign the markers to the players
        print('\n')
        
        turn = choose_first() #to choose who comes first    
        print (turn + ' will go first')
        
        play = input('Are you ready to play? Enter Y or N.\t').upper()
        while play not in ('Y','N'):
            print('The value is not allowed, please insert only "Y" or "N"')
            play = input('Are you ready to play? Enter Y or N.\t').upper()
        
        if play == 'Y': 
            game_on = True
            print('Start the game!')
        else:
            game_on = False
        
        
        while game_on:
            
            #Player 1 Turn
            if turn == 'Player 1':
                print('\nPlayer 1 is your turn')
                
                #Choose a position
                next_position = player_choice(board)
                
                #Place the marker on the position
                place_marker(board, player1, next_position)
                
                #Show the board
                display_board(board)
                
                #Check if there is a win
                if win_check(board, player1):
                    print('\nPlayer 1 HAS WON!')
                    game_on = False
                else:
                    #Check if there is a tie
                    if full_board_check(board) == True:
                        print('\nThe board if full, TIE!')
                        game_on = False
                    else:
                        turn = 'Player 2'          
            
            # Player2's turn.
            else:
                print('\nPlayer 2 is your turn')
                
                #Choose a position
                next_position = player_choice(board)
                
                #Place the marker on the position
                place_marker(board, player2, next_position)
                
                #Show the board
                display_board(board)
                
                #Check if there is a win
                if win_check(board, player2):
                    print('\nPlayer 2 HAS WON!')
                    game_on = False
                else:
                    #Check if there is a tie
                    if full_board_check(board) == True:
                        print('\nThe board if full, TIE!')
                        game_on = False
                    else:
                        turn = 'Player 1' 
            
               
        if not replay():
            break

