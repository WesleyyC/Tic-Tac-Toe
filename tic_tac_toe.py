# A smart Tic Tac Toe player using the strategy in Newell and Simon's 1972 tic-tac-toe program.

######################################################################
####################      Global Variables      ######################
######################################################################
gameBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Testing
count = 0  # Keep track of the filling progress
log = []  # The log of the coordinate
isComputerFirst = 0  # 0 for User go first and 1 for computer go first
UNKNOWN, USER, COMPUTER = range(3)
DIAGONAL_A = [(0, 0), (1, 1), (2, 2)]
DIAGONAL_B = [(0, 2), (1, 1), (2, 0)]
rowWinSum = [0, 0, 0]
columnWinSum = [0, 0, 0]
diagonalASum = 0
diagonalBSum = 0


######################################################################
##############           UI I/O Functions           ##################
######################################################################
def printBoard():
    print ''
    print "    0   1   2"
    print "  +-----------+"
    for row in range(3):
        rowPrint = str(row) + " |"
        for element in gameBoard[row]:
            if element == UNKNOWN:  # Empty Space
                rowPrint += "   |"
            elif element == USER:  # User's Mark
                rowPrint += " X |"
            elif element == COMPUTER:  # Program's Mark
                rowPrint += " O |"
            else:
                print "Something Wrong!!!!"
        print rowPrint
        print "  +-----------+"
    print ''

# Get the coordinate from user
def readCoordinate():
    coordinate = input("Please Give the coordinate of your mark in the form of (row, column) -->")
    if checkCoordinateRange(coordinate):
        return coordinate
    else:
        print ("Please make sure the input coordinate is in range and empty. Try again :)")
        return readCoordinate()


######################################################################
##############             Helper Functions           ################
######################################################################
# Get user input and put mark
def userMove():
    coordinate = readCoordinate()
    putMark(USER, coordinate)

    return coordinate
def putMark(activePlayer, coordinate):
    global count
    count += 1
    logInput(activePlayer, coordinate)
    gameBoard[coordinate[0]][coordinate[1]] = activePlayer

    # Add 4 for program
    # Add 1 for user
    if activePlayer == USER:
        score = 1
    else:
        score = 4

    rowWinSum[coordinate[0]] += score

    columnWinSum[coordinate[1]] += score

    if coordinate in DIAGONAL_A:
        global diagonalASum
        diagonalASum += score

    if coordinate in DIAGONAL_B:
        global diagonalBSum
        diagonalBSum += score

# Only check the three potential win options surrounding the last moved slot #
def checkWinner(newCoordinate):
    # Check Row
    if rowWinSum[newCoordinate[0]] == 3:
        return USER
    elif rowWinSum[newCoordinate[0]] == 12:
        return COMPUTER

    # Check Column
    if columnWinSum[newCoordinate[1]] == 3:
        return USER
    elif columnWinSum[newCoordinate[1]] == 12:
        return COMPUTER

    # Check diagonals:
    if diagonalASum == 3:
        return USER
    elif diagonalASum == 12:
        return COMPUTER

    if diagonalBSum == 3:
        return USER
    elif diagonalBSum == 12:
        return COMPUTER

    return 0

def gameBoardAt(coordinate):
    return gameBoard[coordinate[0]][coordinate[1]]


######################################################################
###############       Tic-Tac-Toe Core Algorithms       ##############
######################################################################
# Rule 1/2: Win/Block
# Check if the program win by putting one mark, or if the user can win by putting one mark
def potentialWinCheck(activePlayer):
    # 4 for program
    # 1 for user
    if activePlayer == USER:
        test = 1
    else:
        test = 4

    # Check row
    for i in range(3):
        if rowWinSum[i] == 2 * test:
            for j in range(3):
                if gameBoard[i][j] == UNKNOWN:
                    return i, j
    # Check column
    for j in range(3):
        if columnWinSum[j] == 2 * test:
            for i in range(3):
                if gameBoard[i][j] == UNKNOWN:
                    return i, j

    # Check diagonal series
    if diagonalASum == 2 * test:
        for i in range(3):
            if gameBoardAt(DIAGONAL_A[i]) == UNKNOWN:
                return DIAGONAL_A[i]

    if diagonalBSum == 2 * test:
        for i in range(3):
            if gameBoardAt(DIAGONAL_B[i]) == UNKNOWN:
                return DIAGONAL_B[i]

    # If no win
    return False

# Rule 3/4:  Fork/Block_Fork
# check the possibility for forking
def fork(activePlayer):
    # threat
    threat = []

    if activePlayer == USER:
        test = 1
    else:
        test = 4

    # Check row
    for i in range(3):
        if rowWinSum[i] == test:
            for j in range(3):
                if gameBoard[i][j] == UNKNOWN:
                    threat.append((i, j))
    # Check column
    for j in range(3):
        if columnWinSum[j] == test:
            for i in range(3):
                if gameBoard[i][j] == UNKNOWN:
                    threat.append((i, j))

    # Check diagonal series
    if diagonalASum == test:
        for i in range(3):
            if gameBoardAt(DIAGONAL_A[i]) == UNKNOWN:
                threat.append(DIAGONAL_A[i])

    if diagonalBSum == test:
        for i in range(3):
            if gameBoardAt(DIAGONAL_B[i]) == UNKNOWN:
                threat.append(DIAGONAL_B[i])

    # Check if there are any repeated threats
    for i in range(len(threat) - 1):
        for j in range(i + 1, len(threat)):
            if threat[i] == threat[j]:
                return threat[i]

    # If no fork
    return False

# Rule 4: Create two-in-a-row
# Cause a two in a row situation to force opponent to defend
# Also prevent opponent from forking whenever possible
def twoInARow(block_fork):
    potential_move = []

    # Check row
    for i in range(3):
        if rowWinSum[i] == 4:
            for j in range(3):
                if gameBoard[i][j] == UNKNOWN:
                    if block_fork == (i, j):
                        return (i, j)
                    else:
                        potential_move.append((i, j))
    # Check column
    for j in range(3):
        if columnWinSum[j] == 4:
            for i in range(3):
                if gameBoard[i][j] == UNKNOWN:
                    if block_fork == (i, j):
                        return (i, j)
                    else:
                        potential_move.append((i, j))

    # Check diagonal series
    if diagonalASum == 4:
        for i in range(3):
            if gameBoardAt(DIAGONAL_A[i]) == UNKNOWN:
                if block_fork == DIAGONAL_A[i]:
                    return DIAGONAL_A[i]
                else:
                    potential_move.append(DIAGONAL_A[i])

    if diagonalBSum == 4:
        for i in range(3):
            if gameBoardAt(DIAGONAL_B[i]) == UNKNOWN:
                if block_fork == DIAGONAL_B[i]:
                    return DIAGONAL_B[i]
                else:
                    potential_move.append(DIAGONAL_B[i])

    if not potential_move:
        return False
    else:
        return potential_move[0]

# Rule 5: Center
def center():
    return gameBoard[1][1] == UNKNOWN

# Rule 6: Opposite Corner
def oppoCorner():
    if gameBoard[0][0] == USER and gameBoard[2][2] == UNKNOWN:
        return 2, 2
    elif gameBoard[2][2] == USER and gameBoard[0][0] == UNKNOWN:
        return 0, 0
    elif gameBoard[0][2] == USER and gameBoard[2][0] == UNKNOWN:
        return 2, 0
    elif gameBoard[2][0] == USER and gameBoard[0][2] == UNKNOWN:
        return 0, 2
    else:
        return False

# Rule 7: Empty Corner
def getCorner():
    if gameBoard[2][2] == UNKNOWN:
        return 2, 2
    elif gameBoard[0][0] == UNKNOWN:
        return 0, 0
    elif gameBoard[2][0] == UNKNOWN:
        return 2, 0
    elif gameBoard[0][2] == UNKNOWN:
        return 0, 2
    else:
        return False

# Rule 8: Empty Side
def getSide():
    if gameBoard[1][0] == UNKNOWN:
        return 1, 0
    elif gameBoard[2][1] == UNKNOWN:
        return 2, 1
    elif gameBoard[1][2] == UNKNOWN:
        return 1, 2
    elif gameBoard[0][1] == UNKNOWN:
        return 0, 1
    else:
        return False

# Computer choice of move based on ordering of rules
def programMove():
    # 1st check if the program can win
    win = potentialWinCheck(COMPUTER)
    if win != False:
        putMark(COMPUTER, win)
        return win
    # 2nd block user's win
    block = potentialWinCheck(USER)
    if block != False:
        putMark(COMPUTER, block)
        return block
    # 3rd try to fork
    programFork = fork(COMPUTER)
    if programFork != False:
        putMark(COMPUTER, programFork)
        return programFork

    # 4th try to block fork by threatening with a two in a row
    userFork = fork(USER)
    if userFork != False:
        tryBlock = twoInARow(userFork)
        if tryBlock != False:
            putMark(COMPUTER, tryBlock)
            return tryBlock
        else:
            putMark(COMPUTER, userFork)
            return userFork

    # 5th put in the center
    if center():
        putMark(COMPUTER, (1, 1))
        return 1, 1
    # 6th try opponent corner
    programOppoCorner = oppoCorner()
    if programOppoCorner != False:
        putMark(COMPUTER, programOppoCorner)
        return programOppoCorner
    # 7th get the corner
    programCorner = getCorner()
    if programCorner != False:
        putMark(COMPUTER, programCorner)
        return programCorner
    # 8th get the side
    programSide = getSide()
    if programSide != False:
        putMark(COMPUTER, programSide)
        return programSide


######################################################################
###################       Just For Sanity           ##################
######################################################################
# A log for gaming progress
def logInput(activePlayer, coordinate):
    log.append(activePlayer)
    log.append(coordinate)

def checkCoordinateRange(coordinate):
    return len(coordinate) == 2 and coordinate[0] < 3 and coordinate[1] < 3 and coordinate[0] >= 0 and coordinate[
                                                                                                           1] >= 0 and \
           gameBoard[coordinate[0]][coordinate[1]] == UNKNOWN
