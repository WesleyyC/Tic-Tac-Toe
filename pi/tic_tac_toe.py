# A perfect Tic Tac Toe player using the strategy in Newell and Simon's 1972 tic-tac-toe program.

# Initial Variable
gameBoard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Testing
count = 0  # Keep track of the filling progress
log = []  # The log of the coordinate
isComputerFirst = 0  # 0 for User go first and 1 for computer go first
UNKNOWN, USER, COMPUTER = range(3)
rowWinSum = [0, 0, 0]
columnWinSum = [0, 0, 0]


# Subject to removal #
# Board Function
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


# why the hell is and else have the same instruction??? #
# A log for gaming progress
def logInput(activePlayer, coordinate):
    log.append(activePlayer)
    log.append(coordinate)


# Put down a mark
def putMark(activePlayer, coordinate):
    global count
    count += 1
    logInput(activePlayer, coordinate)
    gameBoard[coordinate[0]][coordinate[1]] = activePlayer

    # Add 4 for program
    # Add 1 for user
    if activePlayer == USER:
        rowWinSum[coordinate[0]] += 1
        columnWinSum[coordinate[1]] += 1
    elif activePlayer == COMPUTER:
        rowWinSum[coordinate[0]] += 4
        columnWinSum[coordinate[1]] += 4


# Check every possible solution, but might be able to improve
# Give number for each cell and then we can sum each colum or row or diagno to check win.

# Potential optimization: only check the three potential win options surrounding the last moved slot #

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

    # Check diagonal:
    PlayerAtCenter = gameBoard[1][1]
    if (gameBoard[0][0] == PlayerAtCenter and PlayerAtCenter == gameBoard[2][2]) \
            or (gameBoard[0][2] == PlayerAtCenter and PlayerAtCenter == gameBoard[2][0]):
        # Will return 0 when both diagonal is not occupied
        return PlayerAtCenter

    return 0


# Check if the program win by putting one mark, or if the user can win by putting one mark
# If User=True, check if the user can win
def potentialWinCheck(isUser):
    # 4 for program
    # 1 for user
    if isUser:
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
    if gameBoard[0][0] == gameBoard[1][1] and gameBoard[2][2] == UNKNOWN and gameBoard[1][1] == (test + 1) / 2:
        return 2, 2
    if gameBoard[1][1] == gameBoard[2][2] and gameBoard[0][0] == UNKNOWN and gameBoard[2][2] == (test + 1) / 2:
        return 0, 0
    if gameBoard[0][2] == gameBoard[1][1] and gameBoard[2][0] == UNKNOWN and gameBoard[1][1] == (test + 1) / 2:
        return 2, 0
    if gameBoard[1][1] == gameBoard[2][0] and gameBoard[0][2] == UNKNOWN and gameBoard[2][0] == (test + 1) / 2:
        return 0, 2
    if (gameBoard[0][0] == gameBoard[2][2] and gameBoard[1][1] == UNKNOWN and gameBoard[2][2] == (test + 1) / 2) \
            or (gameBoard[0][2] == gameBoard[2][0] and gameBoard[1][1] == UNKNOWN and gameBoard[2][0] == (
                        test + 1) / 2):
        return 1, 1

    # If no win
    return False


# check the possibility for forking
def fork(isUser):
    # threat
    threat = []

    # 2 for program
    # 1 for user
    if isUser:
        test = 1
    else:
        test = 2

    # Counting for winning
    columWin = [0, 0, 0]
    rowWin = [0, 0, 0]

    # Counting for row and column
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == UNKNOWN:
                rowWin[i] += 1
                columWin[j] += 1

    # Check row
    for i in range(3):
        if rowWin[i] == 2:
            for j in range(3):
                if gameBoard[i][j] == test:
                    threat.append((i, (j + 1) % 3))
                    threat.append((i, (j + 2) % 3))
    # Check column
    for j in range(3):
        ##### Why is this twice test instead of 4??? #####
        if columWin[j] == 2 * test:
            for i in range(3):
                if gameBoard[i][j] == test:
                    threat.append(((i + 1) % 3, j))
                    threat.append(((i + 2) % 3, j))

    # Check diagonal series
    if gameBoard[0][0] == gameBoard[1][1] and gameBoard[2][2] == test and gameBoard[1][1] == UNKNOWN:
        threat.append((0, 0))
        threat.append((1, 1))
    if gameBoard[0][0] == gameBoard[2][2] and gameBoard[1][1] == test and gameBoard[2][2] == UNKNOWN:
        threat.append((0, 0))
        threat.append((2, 2))
    if gameBoard[1][1] == gameBoard[2][2] and gameBoard[0][0] == test and gameBoard[2][2] == UNKNOWN:
        threat.append((1, 1))
        threat.append((2, 2))
    if gameBoard[0][2] == gameBoard[1][1] and gameBoard[2][0] == test and gameBoard[1][1] == UNKNOWN:
        threat.append((0, 2))
        threat.append((1, 1))
    if gameBoard[0][2] == gameBoard[2][0] and gameBoard[1][1] == test and gameBoard[2][0] == UNKNOWN:
        threat.append((0, 2))
        threat.append((2, 0))
    if gameBoard[1][1] == gameBoard[2][0] and gameBoard[0][2] == test and gameBoard[2][0] == UNKNOWN:
        threat.append((1, 1))
        threat.append((2, 0))

    for i in range(len(threat) - 1):
        for j in range(i + 1, len(threat)):
            if threat[i] == threat[j]:
                return threat[i]

    # If no fork
    return False


# return the key right next to the current key
def rightNext(n):
    if n == 2:
        return 1
    else:
        return n + 1


# causing a two in a row situation to threat away the fork
# this is basically the fork function but without storing the possible threat
def twoInARow():
    # Counting for winning
    columWin = [0, 0, 0]
    rowWin = [0, 0, 0]

    # Counting for row and column
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == UNKNOWN:
                rowWin[i] += 1
                columWin[j] += 1

    # Check row
    for i in range(3):
        if rowWin[i] == 2:
            for j in range(3):
                if gameBoard[i][j] == COMPUTER:
                    return i, rightNext(j)
    # Check column
    for j in range(3):
        if columWin[j] == 2 * COMPUTER:
            for i in range(3):
                if gameBoard[i][j] == COMPUTER:
                    return rightNext(i), j

    # Check diagonal series
    if gameBoard[0][0] == gameBoard[1][1] and gameBoard[2][2] == COMPUTER and gameBoard[1][1] == UNKNOWN:
        return 1, 1
    if gameBoard[0][0] == gameBoard[2][2] and gameBoard[1][1] == COMPUTER and gameBoard[2][2] == UNKNOWN:
        return 2, 2
    if gameBoard[1][1] == gameBoard[2][2] and gameBoard[0][0] == COMPUTER and gameBoard[2][2] == UNKNOWN:
        return 1, 1
    if gameBoard[0][2] == gameBoard[1][1] and gameBoard[2][0] == COMPUTER and gameBoard[1][1] == UNKNOWN:
        return 1, 1
    if gameBoard[0][2] == gameBoard[2][0] and gameBoard[1][1] == COMPUTER and gameBoard[2][0] == UNKNOWN:
        return 2, 0
    if gameBoard[1][1] == gameBoard[2][0] and gameBoard[0][2] == COMPUTER and gameBoard[2][0] == UNKNOWN:
        return 1, 0

    # If no two in a row
    return False


# User Moving Function
def checkCoordinateRange(coordinate):
    return len(coordinate) == 2 and coordinate[0] < 3 and coordinate[1] < 3 and coordinate[0] >= 0 and coordinate[
                                                                                                           1] >= 0 and \
           gameBoard[coordinate[0]][coordinate[1]] == UNKNOWN


# Get the coordinate from user
def readCoordinate():
    coordinate = input("Please Give the coordinate of your mark in the form of (row, column) -->")
    if checkCoordinateRange(coordinate):
        return coordinate
    else:
        print ("Please make sure the input coordinate is in range and empty. Try again :)")
        return readCoordinate()


# Get user input and putmark
def userMove():
    coordinate = readCoordinate()
    putMark(USER, coordinate)

    return coordinate


# Program Moving Function
def programMove():
    # 1st check if the program can win
    win = potentialWinCheck(False)
    if win != False:
        putMark(COMPUTER, win)
        return win
    # 2nd block user's win
    block = potentialWinCheck(True)
    if block != False:
        putMark(COMPUTER, block)
        return block
    # 3rd try to fork
    programFork = fork(False)
    if programFork != False:
        putMark(COMPUTER, programFork)
        return programFork

    # 4th try to block fork by threatening with a two in a row
    userFork = fork(True)
    if userFork != False:
        tryBlock = twoInARow()
        if tryBlock != False:
            putMark(COMPUTER, tryBlock)
            return tryBlock

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


def center():
    return gameBoard[1][1] == UNKNOWN


# Main Function
def main():
    # Prepare
    winner = UNKNOWN

    # Starter
    print "Welcome to the tic tac toe game!"

    # Loop
    while winner == UNKNOWN and count != 9:
        if count % 2 == isComputerFirst:
            printBoard()
            newCoordinate = userMove()
        else:
            newCoordinate = programMove()
        winner = checkWinner(newCoordinate)

    if winner != UNKNOWN:
        print ''
        print "You Win! And please report you strategy to the author!" if winner == USER else "The Computer Wins!"
    else:
        print ''
        print "It's a tie!"
    printBoard()


if __name__ == '__main__':
    main()
