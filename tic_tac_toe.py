# A perfect Tic Tac Toe player using the strategy in Newell and Simon's 1972 tic-tac-toe program.

# Initial Variable
gameBoard = [[0,0,0],[0,0,0],[0,0,0]]	#Testing
count = 0	# Keep track of the filling progress
log=[]	# The log of the coordinate


# Board Function
def printBoard():
	print "    1   2   3"
	print "  +-----------+"
	for row in range(3):
		rowPrint = str(row+1) + " |"
		for element in gameBoard[row]:
			if element == 0:	# Empty Space
				rowPrint += "   |"
			elif element == 1:	# User's Mark
				rowPrint += " X |"
			elif element == 2:	# Program's Mark
				rowPrint += " O |"
			else:
				print "Something Wrong!!!!"
		print rowPrint
		print "  +-----------+"

# A log for gaming progress
def logInput(user, coordinate):
	if user:
		log.append(coordinate)
	else:
		log.append(coordinate)

# Put down a mark
def putMark(user, coordinate):
	global count 
	count += 1
	logInput(user, coordinate)
	gameBoard[coordinate[0]-1][coordinate[1]-1]= 1 if user else 2

# Check every possible solution, but might be able to improve
# Give number for each cell and then we can sum each colum or row or diagno to check win.
def winCheck():
	# Add 4 for program
	# Add 1 for user
	columWin = [0,0,0]

	# Check row and colum
	for i in range(3):
		# Check Row
		if gameBoard[i] == [1,1,1]:
			return 1
		elif gameBoard[i] == [2,2,2]:
			return 2
		# Mark Column
		for j in range(3):
			if gameBoard[i][j]==1:
				columWin[j] += 1
			elif gameBoard[i][j]==2:
				columWin[j] += 4

	# Check Colum
	for x in columWin:
		if x == 3:
			return 1
		elif x == 12:
			return 2

	# Check Dialogtic:
	centerNum = gameBoard[1][1]
	if(gameBoard[0][0]==centerNum and centerNum ==gameBoard[2][2])or(gameBoard[0][2]==centerNum and centerNum ==gameBoard[2][0]):
		# Will return 0 when both dialogtic is not occupied
		return centerNum

	return 0 

# Check if the program win by putting one mark, or if the user can win by putting one mark
# If User=True, check if the user can win
def potentialWinCheck(User):
	# 4 for program
	# 1 for user
	if User:
		test = 1
	else:
		test = 4

	# Counting for winning
	columWin=[0,0,0]
	rowWin = [0,0,0]

	# Counting for row and column
	for i in range(3):
		for j in range(3):
			if gameBoard[i][j]==2:
				rowWin[i] += 4
				columWin[j] += 4
			elif gameBoard[i][j]==1:
				rowWin[i] += 1
				columWin[j] += 1

	# Check row
	for i in range(3):
		if(rowWin[i]==2*test):
			for j in range(3):
				if(gameBoard[i][j]==0):
					return (i,j)
	# Check column
	for j in range(3):
		if(columWin[j]==2*test):
			for i in range(3):
				if(gameBoard[i][j]==0):
					return (i,j)

	# Check diagnol series
	if(gameBoard[0][0]==gameBoard[1][1] and gameBoard[2][2]==0 and gameBoard[1][1]==(test+1)/2):
		return (2,2)
	if(gameBoard[0][0]==gameBoard[2][2] and gameBoard[1][1]==0 and gameBoard[2][2]==(test+1)/2):
		return (1,1)
	if(gameBoard[1][1]==gameBoard[2][2] and gameBoard[0][0]==0 and gameBoard[2][2]==(test+1)/2):
		return (0,0)
	if(gameBoard[0][2]==gameBoard[1][1] and gameBoard[2][0]==0 and gameBoard[1][1]==(test+1)/2):
		return (2,0)
	if(gameBoard[0][2]==gameBoard[2][0] and gameBoard[1][1]==0 and gameBoard[2][0]==(test+1)/2):
		return (1,1)
	if(gameBoard[1][1]==gameBoard[2][0] and gameBoard[0][2]==0 and gameBoard[2][0]==(test+1)/2):
		return (0,2)

	# If no win
	return False

def rightNext(i):
	if i == 1:
		return 2
	else:
		return 1

# check the possibility for forking
def fork(User):
	# threat
	threat=[]

	# 4 for program
	# 1 for user
	if User:
		test = 1
	else:
		test = 2

	# Counting for winning
	columWin=[0,0,0]
	rowWin = [0,0,0]

	# Counting for row and column
	for i in range(3):
		for j in range(3):
			if gameBoard[i][j]==0:
				rowWin[i] += 1
				columWin[j] += 1


	# Check row
	for i in range(3):
		if(rowWin[i]==2):
			for j in range(3):
				if(gameBoard[i][j]==test):
					threat.append((i,rightNext(j)))
	# Check column
	for j in range(3):
		if(columWin[j]==2*test):
			for i in range(3):
				if(gameBoard[i][j]==test):
					threat.append((rightNext(i),j))

	# Check diagnol series
	if(gameBoard[0][0]==gameBoard[1][1] and gameBoard[2][2]==test and gameBoard[1][1]==0):
		threat.append((1,1))
	if(gameBoard[0][0]==gameBoard[2][2] and gameBoard[1][1]==test and gameBoard[2][2]==0):
		threat.append((2,2))
	if(gameBoard[1][1]==gameBoard[2][2] and gameBoard[0][0]==test and gameBoard[2][2]==0):
		threat.append((1,1))
	if(gameBoard[0][2]==gameBoard[1][1] and gameBoard[2][0]==test and gameBoard[1][1]==0):
		threat.append((1,1))
	if(gameBoard[0][2]==gameBoard[2][0] and gameBoard[1][1]==test and gameBoard[2][0]==0):
		threat.append((2,2))
	if(gameBoard[1][1]==gameBoard[2][0] and gameBoard[0][2]==test and gameBoard[2][0]==0):
		threat.append((1,1))

	for i in range(len(threat)-1):
		for j in range(i+1,len(threat)):
			if(threat[i]==threat[j]):
				return threat[i]

	# If no fork
	return False


# User Moving Function
def checkCoordinateRange(coordinate):
	return len(coordinate)==2 and coordinate[0]<=3 and coordinate[1]<=3 and coordinate[0]>0 and coordinate[1]>0 and gameBoard[coordinate[0]-1][coordinate[1]-1]==0

# Get the coordinate from user
def readCoordinate():
	coordinate = input("Please Give the coordinate of your mark in the form of (row, column) -->")
	if(checkCoordinateRange(coordinate)):
		return coordinate
	else:
		print ("Please make sure the input coordinate is in range and empty. Try again :)")
		readCoordinate()

# Get user input and putmark
def userMove():
	coordinate = readCoordinate()
	putMark(True, coordinate)


# Program Moving Function
def programMove():
	# In case the program double move
	notPut = True;
	# 1st check if the program can win
	win = potentialWinCheck(False)
	if (win!=False and notPut):
		putMark(False,programCoordinate(win))
		notPut = False
	# 2ne block user's win
	block = potentialWinCheck(True)
	if (block!=False and notPut):
		putMark(False,programCoordinate(block))
		notPut = False
	# 3rd try to fork
	programFork = fork(False)
	if (programFork!=False and notPut):
		putMark(False,programCoordinate(programFork))
		notPut = False
	# 4th try to block fork
	userFork = fork(True)
	if (userFork!=False and notPut):
		putMark(False,programCoordinate(userFork))
		notPut = False
	# 5th put in the center
	if (center() and notPut):
		putMark(False,(2,2))
		notPut = False
	# 6th try opponent corner
	programOppoCorner = oppoCorner()
	if (programOppoCorner!=False and notPut):
		putMark(False,programCoordinate(programOppoCorner))
		notPut = False
	# 7th get the corner
	programCorner = getCorner()
	if (programCorner!=False and notPut):
		putMark(False,programCoordinate(programCorner))
		notPut = False
	# 8th get the side
	programSide = getSide()
	if (programSide!=False and notPut):
		putMark(False,programCoordinate(programSide))
		notPut = False
	# check there is a put
	if notPut:
		print("Something is wrong!!");

def getSide():
	if gameBoard[1][0]==0:
		return (1,0)
	elif gameBoard[2][1]==0:
		return (2,1)
	elif gameBoard[1][2]==0 :
		return (1,2)
	elif gameBoard[0][1]==0:
		return (0,1)
	else:
		return False

def getCorner():
	if gameBoard[2][2]==0:
		return (2,2)
	elif gameBoard[0][0]==0:
		return (0,0)
	elif gameBoard[2][0]==0 :
		return (2,0)
	elif gameBoard[0][2]==0:
		return (0,2)
	else:
		return False

def oppoCorner():
	if(gameBoard[0][0]==1 and gameBoard[2][2]==0):
		return (2,2)
	elif(gameBoard[2][2]==1 and gameBoard[0][0]==0):
		return (0,0)
	elif(gameBoard[0][2]==1 and gameBoard[2][0]==0):
		return (2,0)
	elif(gameBoard[2][0]==1 and gameBoard[0][2]==0):
		return (0,2)
	else:
		return False

def center():
	return gameBoard[1][1]==0

# the purMark are optimized for user, so we need to increment the coor that program generate
def programCoordinate(coor):
	return (coor[0]+1,coor[1]+1)

# Main Function
def main():
	# Prepare
	winner = 0

	# Starter
	print "Welcome to the tic tac toe game!"

	# Loop
	while (winner == 0 and count!=9):
		printBoard()
		userMove()
		programMove()
		winner = winCheck()

	if winner != 0:
		print ''
		print "You Win!" if winner == 1 else "The Computer Wins!"
	else:
		print ''
		print "It's a tie!"
	printBoard()

if __name__ == '__main__':
	main()
