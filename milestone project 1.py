f0 = [' ', ' ', ' ']
f1 = [' ', ' ', ' ']
f2 = [' ', ' ', ' ']
board = [f0, f1, f2]
players = ['X', '0']
moves = 1
player = 0
winner = -1


def print_board(l):
    #first line
    print " {p0} | {p1} | {p2} ".format(p0=l[0][0], p1=l[0][1], p2=l[0][2])
    print "-----------"
    print " {p0} | {p1} | {p2} ".format(p0=l[1][0], p1=l[1][1], p2=l[1][2])
    print "-----------"
    print " {p0} | {p1} | {p2} ".format(p0=l[2][0], p1=l[2][1], p2=l[2][2])


def get_first_player(p):
    usrInput = raw_input("Who is going to start playing? (X / 0): ")
    while usrInput not in p:
        usrInput = raw_input("That's not a valid a player, try again (X / 0): ")

    return players.index(usrInput)


def get_position(b):
    valid_position = False
    while not valid_position:
        x = int(raw_input("Enter row number (1,2,3) :"))
        while x not in [1, 2, 3]:
            x = raw_input("Not a valid position for the row, try again:")

        y = int(raw_input("Enter column number (1,2,3) :"))
        while y not in [1, 2, 3]:
            y = raw_input("Not a valid position for the column, try again:")

        if b[x-1][y-1] == ' ':
            valid_position = True
        else:
            print "That position was already taken, try again!\n"

    return [x, y]


def evaluate_move(pos, b):
    value = b[pos[0]][pos[1]]

    #look in the row
    if len(set(b[pos[0]])) <= 1:
        return True

    #look in the column
    if len([row[pos[1]] for row in b]) <= 1:
        return True


    #look in the diagonals
    if (pos[0] == pos[1]) or (pos[0] + pos[1] == 2):
        if (pos[0] == pos[1]) and (pos[0] + pos[1] == 2):
            if b[0][0] == b[1][1] == b[2][2]:
                return True
            if b[0][2] == b[1][1] == b[2][0]:
                return True
        elif (pos[0] == pos[1]) and (pos[0] + pos[1] != 2):
            if b[0][0] == b[1][1] == b[2][2]:
                return True
        else:
            if b[0][2] == b[1][1] == b[2][0]:
                return True

    return False


player = get_first_player(players)

while winner == -1 and moves <= 9:
    print_board(board)
    print "Move {move} | Player {p}".format(move=moves, p=players[player])
    position = get_position(board)
    print "Your position is X: {}, Y: {}".format(position[0], position[1])

    #get real index position into the matrix (starting by index 0 not 1)
    position = [position[0]-1, position[1]-1]

    #write move into the board
    board[position[0]][position[1]] = players[player]

    if evaluate_move(position, board):
        winner = player

    #switch player
    player = 1 if player == 0 else 0
    moves += 1
    print "\n"


print_board(board)
if winner != -1:
    print "The Winner is {p}!!!".format(p=players[winner])
else:
    print "The game has ended with no winner :( "
