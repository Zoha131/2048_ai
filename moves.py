import random


#initialize board
def init_board():
    board = []
    for i in range(4):
        board += [["0"] * 4]

    # Init with two numbers.
    addNewNum(board, 2)

    #debugging code

    """
    board[0][0] = "0"
    board[0][1] = "0"
    board[0][2] = "8"
    board[0][3] = "0"
    board[1][0] = "0"
    board[1][1] = "8"
    board[1][2] = "0"
    board[1][3] = "64" 
    board[2][0] = "0"   
    board[2][1] = "2"
    board[2][2] = "32"
    board[2][3] = "256"
    board[3][0] = "0"
    board[3][1] = "16"  
    board[3][2] = "1024"
    board[3][3] = "1024"   
    """

    return board


auto_s = [2,4,2,4,4,2,4,2,4,2,2,4,4,4,4,2,4,2,4,4,2,2,4,2,2,4,4,4,2,4,4,2,4,4,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2,4,2,4,2,2,
          4,2,4,2,2,2,4,2,4,2,4,4,2,2,2]
auto_y = [1,1,3,3,0,0,2,1,1,2,2,0,2,0,0,1,0,1,0,3,0,0,0,2,3,1,0,1,3,0,1,3,3,3,3,0,0,0,1,2,3,1,3,3,0,2,0,0,0,3,3,3,3,3,3,
          3,3,3,0,3,0,1,1,0,0,1,0,1,0,1]
auto_x = [0,2,1,2,1,3,2,3,1,3,1,2,3,0,3,3,3,3,0,3,3,3,2,2,3,2,0,2,3,0,0,3,3,2,3,0,3,3,0,0,3,2,0,3,3,3,3,3,2,3,0,0,3,3,0,
          1,0,3,3,1,0,3,0,3,3,3,0,0,3,0]
auto_moves = ["d","l","l","d","l","d","d","d","d","l","l","d","l","l","l","d","r","l", "d", "l","l","l","d","d","d","l",
              "d","r","l","d","u","l","d","r","l","d","r","l","d","r","u","l","d","l","d","l","d","u","r","u","l","u","r",
              "u","u","l","d","u","d","l","r","l","d","l","r","d","l","r"]

index = 0



def addNewNum(board, n):

    """Generates a 2 or 4, and set the number at a random location on board \
    that is originally a 0.
    """
    global index

    for i in range(n):
        newNum = str(auto_s[index])
        randomx = auto_x[index]
        randomy = auto_y[index]

        board[randomy][randomx] = newNum
        print("x: "+str(randomx)+" y:"+str(randomy), " num:"+str(newNum))
        index = index+1


def checkWin(board):

    """ Checks if the player has the number 2048 on the board.
    If so, return True. Otherwise, return False.
    """

    win = False
    for line in board:
        for num in line:
            if num == "2048":
                win = True
    return win


def add(board, i_list, j_list, i_direction, j_direction):

    """Iterates through the board, and adds a number with its adjacent neighbor if the two numbers are the same.
    ex. 2248 becomes 0448.
    i_list, j_list - lists, indicate how add interate through the list.
    i_direction, j_direction - an int, either 1, -1 or 0. Defines the direction of the add. 
    ex. +1, 2248 becomes 0448. -1, 2248 becomes 4480, 0, does not add. 
    
    move is a counter that's later used to determine whether a move can still be made by the player.
    """

    move = 0
    for i in i_list:
        for j in j_list:

        #check if 2 numbers are the same, if yes, add them together
            if board[i][j] == board[i + i_direction][j + j_direction]:
                board[i+ i_direction][j + j_direction] = str(int(board[i][j])+int(board[i+ i_direction][j+j_direction]))
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def push(board, i_list, j_list, i_direction, j_direction):

    """Push a number to its adjacent slot if the slot is 0.
    i_list, j_list - lists, indicate how push interate through the list.
    i_direction, j_direction - an int, either 1, -1 or 0. Defines the direction of the push. 
    move is a counter that's later used to determine whether a move can still be made by the player.
    """

    move = 0
    for i in i_list:
        for j in j_list:
            if board[i + i_direction][j + j_direction] == "0":
                board[i + i_direction][j + j_direction] = board[i][j]
                if board[i][j] != 0:
                    move += 1
                board[i][j] = "0"
    return move


def pushDirection(board, UserInput):
    """Takes in a UserInput and calls add and push function with the proper i_list,\
    j_list, i_direction and j_direction. 
    UserInput - a str
    """

    move = 0
    if UserInput == "u":
        i_list, j_list = range(1,4), range(4)
        i_direction, j_direction = -1, 0
    elif UserInput == "d":
        i_list, j_list = range(2,-1,-1), range(4)
        i_direction, j_direction = 1, 0
    elif UserInput == "l":
        i_list, j_list = range(4), range(1,4)
        i_direction, j_direction = 0, -1
    elif UserInput == "r":
        i_list, j_list = range(4), range(2,-1,-1)
        i_direction, j_direction = 0, 1

    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)

    move += add(board, i_list, j_list, i_direction, j_direction)

    for i in range(4):
        move += push(board, i_list, j_list, i_direction, j_direction)

    return move


def checkCell(board, i, j):
    """Checks the cell above/ below/ to the left/ to the right
    of board[i][j] and see if one or more equals to board[i][j]
    if so, return True.
    else, return False.
    """

    move_i = []
    move_j = []
    board_size = len(board)
    if i > 0:
        move_i.append(-1)
        move_j.append(0)
    if i < (board_size - 1):
        move_i.append(1)
        move_j.append(0)
    if j > 0:
        move_j.append(-1)
        move_i.append(0)
    if j < (board_size - 1):
        move_j.append(1)
        move_i.append(0)
    for k in range(len(move_i)):
        if board[i + move_i[k]][j + move_j[k]] == board[i][j]:
            return True
    return False


def canMove(board):
    """Checks if the player can still can still make a move.
    If so, return True. Else, return False.
    """

    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                return True
            if checkCell(board, i, j):
                return True
    return False

def checkLose(board):

    """Takes in a list (board), return True the player does not lose
    (if there is still 0 in the list or \ if any move can still be made)
    otherwise False
    """

    nozero = False

    for elt in board:
        nozero = nozero or ("0" in elt)

    if not nozero:
        return not canMove(board)
    return False


def main(board, UserInput):

    if not checkLose(board) and not checkWin(board):

        move = pushDirection(board, UserInput)
        if move != 0:
            addNewNum(board, 1)
    return board



