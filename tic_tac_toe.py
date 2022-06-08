# tic-tac-toe

from random import randrange

board = '--------------------'
print("This is a playing field. The maximum position is", len(board))


def evaluate(board):
    
    if board.find('xxx') != -1:
        return 'x'

    elif board.find('ooo') != -1:
        return 'o'

    elif board.find('-') == -1:
        return '!'
    
    else:
        return '-'

def move(board, position, mark):
    if position == 1:
        return mark + board[position:]    
    else:
        return board[:position - 1] + mark + board[position:]

def player_move(board):
    position = int(input("Which position you wants to play? "))
    mark = 'x'
    while(True):
        lenght_board = len(board)
        if position <= 0 or position > lenght_board:
            print("It is impossible position. Try again. ") 
            position = int(input("Which position you wants to play? "))
        else:
           
            if board[position - 1] == "-":
                return move(board, position, mark)
            else:
                print('This position has already been used. Choose another position: ')
                position = int(input("Which position you wants to play? "))


def pc_defend(board):
    
    position_defend = board.find('x-x')
    if position_defend != -1:
        return position_defend + 1 + 1
    
    position_defend = board.find('-x')    
    if position_defend != -1:
        return position_defend + 1
    
    position_defend = board.find('x-')
    if position_defend != -1:
        return position_defend + 1 + 1    
    
    return -1


def pc_attack(board):
    lenght_board = len(board)

    position_attack = board.find('o-o')
    if position_attack != -1:
        return position_attack + 1 + 1
    
    position_attack = board.find('-o')    
    if position_attack != -1:
        return position_attack + 1
    
    position_attack = board.find('o-')
    if position_attack != -1:
        return position_attack + 2 + 1    

    return randrange(lenght_board - 1)

def pc_move(board):
    mark = 'o'
    position_defend = pc_defend(board)
    position_attack = pc_attack(board)
    
    if position_defend != -1:
        print("PC made a choice", position_defend)
        return move(board, position_defend, mark)
    else:
        print("PC made a choice", position_attack)
        return move(board, position_attack, mark)
    
     
def game_manager(board):
    print(board)
    while (True):
        board = player_move(board)     
        if evaluate(board) == 'x':
            print(board)
            print("You are won.")
            break
        elif evaluate(board) == 'o':
            print(board)
            print("PC is won.")
            break
        elif evaluate(board) == '!':
            print(board)
            print("Draw.")
            break   
        else:
            print(board) 
        
        board = pc_move(board)
        if evaluate(board) == 'x':
            print(board)
            print("You are won.")
            break
        elif evaluate(board) == 'o':
            print(board)
            print("PC is won.")
            break
        elif evaluate(board) == '!':
            print(board)
            print("Draw.")
            break    
        else:
            print(board) 

game_manager(board)
