import random

def TMA3():
    playerDict = {} #Player dictionary with players as keys, scores as values
    playerNo = 0   
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
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
    gridSize = 0
    totalCells = 0
    while True:
        gameNo = input("Enter game level(1 to 2): ")
        if gameNo == "1":            
            gridSize = 4   
            print("Grid size: ", gridSize)         
            break
        elif gameNo == "2":            
            gridSize = int(input("Enter grid size(2 to 7): "))            
            if gridSize < 2 or gridSize > 7:
                print("Please enter a valid grid size")
            else:                 
                print("Grid size: ", gridSize)    
                break
        print("Please enter a valid game level")
    totalCells = gridSize*gridSize
	#Populate the grid	
    cellChoices = [] 
	
    for i in range(totalCells):
        grid[i] = "NIL"
        cellChoices.append(i)
	
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
            cellNo = random.choice(cellChoices) #Randomly choose a cell number			
            grid[cellNo] = letter
            cellChoices.remove(cellNo)

    print("*** Cheat Sheet ***")
    print("       Columns")
    print('Rows | {} | {} | {} | {} |'.format(1, 2, 3, 4))
    print("-----------------------")    
    rowCount = 1
    i = 0
    while i < totalCells:
        line = "   " + str(rowCount) + " | "
        for j in range(gridSize):
            line += grid[i] + " | "
            i = i+1
        print(line)
        rowCount += 1      

TMA3()
