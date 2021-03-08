import random

def TMA3():
	playerDict = {} #Player dictionary with players as keys, scores as values
	playerNo = 0   
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	grid = {} #Grid dictionary with cell numbers as keys, letters as values
	
	while playerNo < 4:
		playerName = input("Enter player name or <ENTER> to exit (min 2, max 4 players): ")
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
	gridSize = int()
	while True:
		gameNo = input("Enter game level(1 to 2): ")
		if gameNo == "1":
			gridSize = 16
			break
		elif gameNo == "2":
			gridSize = int(input("Enter grid size(2 to 7): "))
			if gridSize < 2 or gridSize > 7:
				print("Please enter a valid grid size")
			else: 
				break
		print("Please enter a valid game level")
	
	#Populate the grid	
	gridChoices = [] 
	
	for i in range(gridSize):
		grid[i] = ""
		cellChoices.append(i)
	
	while gridChoices:
		letter = random.choice(letters) #Randomly choose a letter from the list letters
		twoOrFour = random.randint(0,1) #If twoOrFour == 0, assign the letter to 2 cards, if twoOrFour == 1, assign the letter to 4 cards
		loopNo = 0
		if twoOrFour == 0:
			loopNo = 2
		elif twoOrFour == 1:
			loopNo = 4
		for i in range(loopNo):
			cellNo = random.choice(cellChoices) #Randomly choose a cell number
			if grid[cellNo] != "":
				grid[cellNo] = letter
TMA3()
