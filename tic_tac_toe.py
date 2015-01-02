# A perfect tic_tac_toe player
#gameBoard = [[0,0,0],[0,0,0],[0,0,0]]
gameBoard = [[1,0,1],[2,2,0],[2,0,1]]
log=[[]]
# graphDic = {}

def logInput(user, coordinate):
	if user:
		log.append(coordinate)
	else:
		log.append(coordinate)


# Can be imrpoved
# Check every possible solution
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

	# Check Dialog:
	centerNum = gameBoard[1][1]
	if(gameBoard[0][0]==centerNum and centerNum ==gameBoard[2][2])or(gameBoard[0][2]==centerNum and centerNum ==gameBoard[2][0]):
		# Will return 0 when both dialogs is not occupied
		return centerNum

	return 0 

# def checkGraphRange(coordinate):
# 	return len(coordinate)==2 and coordinate[0]<3 and coordinate[1]<3 and coordinate[0]>=0 and coordinate[1]>=0

# def createGraphDic():
# 	for i in range(3):
# 		for j in range(3):
# 			graphDic[(i,j)]=[]
# 			if(checkGraphRange((i+1,j))):
# 				graphDic[(i,j)].append((i+1,j))
# 			if(checkGraphRange((i+1,j+1))):
# 				graphDic[(i,j)].append((i+1,j+1))
# 			if(checkGraphRange((i,j+1))):
# 				graphDic[(i,j)].append((i,j+1))

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
	logInput(True, coordinate)
	gameBoard[coordinate[0]-1][coordinate[1]-1]=1

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

def main():
	# Prepare
	#///////////////createGraphDic()
	winner = 0

	# Starter
	print "Welcome to the tic tac toe game!"

	# Loop
	while winner == 0:
		printBoard()
		userMove()
		winner = winCheck()

	print ''
	print "You Win!" if winner == 1 else "The Computer Wins!"
	printBoard()


if __name__ == '__main__':
	main()
	#print winCheck()