# A perfect Tic Tac Toe player using the strategy in Newell and Simon's 1972 tic-tac-toe program.

# Initial Variable
#gameBoard = [[0,0,0],[0,0,0],[0,0,0]]	# The Game Board
gameBoard = [[1,0,1],[2,2,0],[2,0,1]]	#Testing
log=[]	# The log of the coordinate
# graphDic = {}	# Graph


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

def logInput(user, coordinate):
	if user:
		log.append(coordinate)
	else:
		log.append(coordinate)

def putMark(user, coordinate):
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

'''
def checkGraphRange(coordinate):
	return len(coordinate)==2 and coordinate[0]<3 and coordinate[1]<3 and coordinate[0]>=0 and coordinate[1]>=0

def createGraphDic():
	for i in range(3):
		for j in range(3):
			graphDic[(i,j)]=[]
			if(checkGraphRange((i+1,j))):
				graphDic[(i,j)].append((i+1,j))
			if(checkGraphRange((i+1,j+1))):
				graphDic[(i,j)].append((i+1,j+1))
			if(checkGraphRange((i,j+1))):
				graphDic[(i,j)].append((i,j+1))
'''

# User Moving Function
def checkCoordinateRange(coordinate):
	return len(coordinate)==2 and coordinate[0]<=3 and coordinate[1]<=3 and coordinate[0]>0 and coordinate[1]>0 and gameBoard[coordinate[0]-1][coordinate[1]-1]==0

def readCoordinate():
	coordinate = input("Please Give the coordinate of your mark in the form of (row, column) -->")
	if(checkCoordinateRange(coordinate)):
		return coordinate
	else:
		print ("Please make sure the input coordinate is in range and empty. Try again :)")
		readCoordinate()

def userMove():
	coordinate = readCoordinate()
	putMark(True, coordinate)


# Program Moving Function
def programMove():
	

# Main Function
def main():
	# Prepare
	#createGraphDic()
	winner = 0

	# Starter
	print "Welcome to the tic tac toe game!"

	# Loop
	while winner == 0:
		printBoard()
		userMove()
		programMove()
		winner = winCheck()

	print ''
	print "You Win!" if winner == 1 else "The Computer Wins!"
	printBoard()


if __name__ == '__main__':
	main()
