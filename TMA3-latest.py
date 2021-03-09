import random

def validateInput(row_colStr, gridSize, facedUp):
	#Check the input
	row_colList = row_colStr.split() #[0] is the row number, [1] is the column number
	row = int(row_colList[0])
	col = int(row_colList[1])
	if row > 0 and row <= gridSize and col > 0 and col <= gridSize:
		#Check if the cell is NIL
		if row == gridSize and col == gridSize and gridSize%2 != 0:
			print(f"Please choose a different row and column that is not for NIL")
			return "invalid"		
		#Check if the cell is already faced up
		else:
			cellNo = int("".join(row_colList))
			if facedUp[cellNo] == True:
				print(f"Please choose a card that is not face up yet")
				return "invalid"
			else:
				return "valid"
	else:
		print(f"Please choose a card row and column within the grid")
		return "invalid"

def printGrid(gridSize, facedUp, grid):
	#Print out the grid
	print("       Columns")
	print('Rows | {} | {} | {} | {} |'.format(1, 2, 3, 4))
	print("-----------------------")    
	rowNo = 1	
	while rowNo <= gridSize:
		cellNo = rowNo*10 + 1
		line = "   " + str(rowNo) + " | "
		#Loop through the current row
		for i in range(gridSize):
			if facedUp[cellNo] == True:
				line += grid[cellNo] + " | "			
			else:
				line += "  | "
			cellNo+=1
		print(line)
		rowNo += 1	  
	print("-----------------------") 
		
def TMA3():
	playerDict = {} #Player dictionary with players as keys, scores as values
	playerNo = 0   
	letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	grid = {} #Grid dictionary with cell numbers as keys, letters as values
	
	while playerNo < 4:
		playerName = input("Enter player name or <ENTER> to exit (min 2, max 4 players): ")
		playerName = playerName.upper()
		#validate name
		if playerName in playerDict:
			print("Repeated name. Choose another name")
		elif playerName != "":
			playerNo += 1
			playerDict[playerName] = 0
			print(f"Minimum 2 players. Currently, {playerNo} player")
		elif playerName == "":
			break
		
	gameNo = int()
	gridSize = 0
	totalCells = 0
	while True:
		gameNo = input("Enter game level(1 to 2): ")
		if gameNo == "1":            
			gridSize = 4           
			break
		elif gameNo == "2":            
			gridSize = int(input("Enter grid size(2 to 7): "))            
			if gridSize < 2 or gridSize > 7:
				print("Please enter a valid grid size")
			else:                 				 
				break
		elif gameNo == "":
			break
		else:
			print("Please enter a valid game level")	
	print("Grid size: ", gridSize)  
	#Populate the grid and initialise all the cells to face down, that is facedUp[cellNo] = False
	cellChoices = [] 	
	facedUp = {}
	rowNo = 1 
	while rowNo <= gridSize:
		cellNo = rowNo*10 + 1 #cellNos are 11, 12, 13, 14, 21, 22, 23, 24 etc.
		#Loop through the current row
		for i in range(gridSize):
			grid[cellNo] = "NIL"
			cellChoices.append(cellNo)
			facedUp[cellNo] = False
			cellNo+=1
		rowNo += 1
	totalCells = gridSize*gridSize
	if totalCells%2 != 0: #Keep the last cell as NIL
		totalCells -= 1 
		cellChoices.pop(-1) 
		
	while cellChoices: #Exit while loop when cellChoices becomes empty
		letter = random.choice(letters) #Randomly choose a letter from the list letters
		letters.remove(letter)
		twoOrFour = random.randint(0,1) #If twoOrFour == 0, assign the letter to 2 cards, if twoOrFour == 1, assign the letter to 4 cards
		loopNo = 0
		if twoOrFour == 0:
			loopNo = 2
		elif twoOrFour == 1:
			loopNo = 4
        #Assign the letter to 2 or 4 cells
		for i in range(loopNo):			
			if cellChoices:
				cellNo = random.choice(cellChoices) #Randomly choose a cell number			
				grid[cellNo] = letter
				cellChoices.remove(cellNo)
			else:
				break

	print("*** Cheat Sheet ***")
	print("       Columns")
	print('Rows | {} | {} | {} | {} |'.format(1, 2, 3, 4))
	print("-----------------------")    
	rowNo = 1	
	while rowNo <= gridSize:
		cellNo = rowNo*10 + 1
		line = "   " + str(rowNo) + " | "
		#Loop through the current row
		for i in range(gridSize):
			line += grid[cellNo] + " | "			
			cellNo+=1
		print(line)
		rowNo += 1	  
	print("-----------------------")    
	print("*** End of Cheat Sheet ***")
	
	print("*** Starting a new game ***")
	print("       Columns")
	print('Rows | {} | {} | {} | {} |'.format(1, 2, 3, 4))
	print("-----------------------")    
	rowCount = 1
	i = 0
	while i < totalCells:
		line = "   " + str(rowCount) + " | "
		for j in range(gridSize):
			line += "  | "
			i = i+1
		print(line)
		rowCount += 1      
	print("-----------------------")  
	
	correctPairs = 0
	noOfPairs = int(totalCells/2)
		
	while correctPairs < noOfPairs:
		#Loop through playerDict
		for player in playerDict.keys():
			print(f"Player {player}, enter your guess")
			print(f"Current number of correct pairs: {correctPairs}")
			while True:
				row_colStr1 = str(input("Enter first card row and column, separated by space:")).strip()
				if validateInput(row_colStr1, gridSize, facedUp) == "valid":
					cellNo1 = int("".join((row_colStr1).split()))
					cellVal1 = grid[cellNo1]
					print(f"Open {cellVal1}")
					row_colStr2 = ""
					while True:
						row_colStr2 = str(input("Enter second card row and column, separated by space:")).strip()
						if row_colStr2 == row_colStr1:
							print(f"Please choose a different row and column from your earlier choice")		
						else:
							break
					if validateInput(row_colStr2, gridSize, facedUp) == "valid":						
						cellNo2 = int("".join((row_colStr2).split()))
						cellVal2 = grid[cellNo2]
						print(f"Open {cellVal2}")
						if cellVal1 == cellVal2:
							correctPairs+=1								
							playerDict[player] += 1
							facedUp[cellNo1] = True
							facedUp[cellNo2] = True
							print(f"Correct")
							print(f"Updated number of correct pairs: {correctPairs}")								 
							#Print out the grid
							printGrid(gridSize, facedUp, grid)
							#Check to end the game
							if correctPairs == noOfPairs:
								print(f"Game ends!")
								break
						else: #Wrong guess
							print(f"Non-matching. No update")
							break
								
			#Print out the grid
			printGrid(gridSize, facedUp, grid)
	
	scores = list(playerDict.values())
	players = list(playerDict.keys())
	maxScore = max(scores)
	playerWithMaxScore = players[scores.index[maxScore]]
	print(f"Winners with {maxScore} matched pairs: {playerWithMaxScore}")
		
	#Repeat the game
	print(f"Play again? <ENTER> an empty string to play again:")
TMA3()