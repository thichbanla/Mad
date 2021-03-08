def getPartsInCode(productCode):
    partIds = "ABCDEFGHIJKL"
    format = ""
    for n in range(len(productCode)):
        if productCode[n] in partIds:
            if productCode[n] == 0 or productCode[n] != productCode[n-1]:
                format+= str(productCode.count(productCode[n])) + productCode[n] + " "
    return format

def validateInput(newProductCode, partIds):  
    if len(newProductCode)<3:    
        return "invalid"
    else:
        count = 1
        currCode = newProductCode[0]
		#Check if the code consists of at least 3 parts
        for c in newProductCode:
            if c != currCode: #An unique code
                count+=1
        if count < 3:
            return "invalid"
        else:
			#Check if each character is a letter from A to L.            
            for c in newProductCode:                
                if c not in partIds:        
                    return "invalid"
            #Iterated through all characters in newProductCode, all chars are valid, newProductCode is valid
            return "valid"

def TMA2b():
	startLevel=100
	reorderPoint=20
	partIds="ABCDEFGHIJKL"
	stock = [startLevel,startLevel,startLevel,startLevel,startLevel,startLevel,startLevel,startLevel,startLevel,startLevel,startLevel,startLevel]
	productCodes = []
	print("Menu")
	print("1. Add product code")
	print("2. List inventory")
	print("3. Update inventory")
	print("4. Make Product")
	print("5. Get summarised data")
	print("0. Exit")
	while True:
		Option = input("Select Menu Option: ")
		if Option == "1": #Add product code      
			productCode = str(input("Enter new product code: ").upper())
			''.join(sorted(productCode)) #To sort product code alphabetically
			#Validate the input
			if validateInput(productCode, partIds) == "invalid":
				print("The product code is invalid")
			elif productCode.upper() in productCodes:      
				print("The product code already exist")
			else:
				productCodes.append(productCode.upper())
				print("The product code has been added successfully")

		elif Option == "2": #List inventory
			print('Part Stock Level')
			for n in range(len(partIds)):
				print(f'{partIds[n]:3s} {stock[n]:5d}', end='')
				if stock[n] <= reorderPoint:
					print('  ***')
				else:
					print()

		elif Option == "3": #Update inventory
			updated = []
			while True:
				identifier = input("Enter part identifier or <ENTER> to end: ").upper()
				if identifier not in partIds:
					print("The part identifier is invalid")      
				elif identifier == "":
					return      
				else:
					index=partIds.find(identifier)
					print(f"Current stock level for {identifier} = {stock[index]}")
					quantity = int(input("Enter quantity to add: "))
					if quantity <= 0:
						print("The quantity is invalid")
					else:
						stock[index] += quantity
						print(f"Updated stock level for {identifier} = {stock[index]}")
						updated.append([identifier,quantity])
			fw=open("transactions.txt","a")
			for identifier,quantity in updated:
				print(f"restock {identifier} {quantity}", file=fw)
			fw.close()

		elif Option == "4": #Make Product
			makeProduct = input(f"Enter product code: ")
			makeProduct = makeProduct.upper()
			''.join(sorted(makeProduct)) #To sort product code alphabetically
			#Validate the input
			if validateInput(makeProduct, partIds) == "valid":
				makeQuantity = int(input(f"Enter quantity to make: "))
				if makeQuantity < 1:
					print(f"Invalid quantity {makeQuantity}")
			   
				#Check the stock and prepare to make the new product  
				else:         
					partDict = {} #Store all parts in the new product together with their required quantity
					qtyAndPartStr = getPartsInCode(makeProduct)
					#Analyse qtyAndParts, e.g. 1A 2B 3C
					spaceIndex = -1 #Store the index of the last space iterated
					partCode = ""
					qtyInCode = 0
					for n in range(len(qtyAndPartStr)):
						if qtyAndPartStr[n] == " ":
							spaceIndex = n
						if qtyAndPartStr[n] in partIds: #Get the part code
							partCode = qtyAndPartStr[n]
							qtyInCode = int(qtyAndPartStr[spaceIndex+1:n])							
							partDict[partCode] = qtyInCode 					

					#Check the stock
					productAvail = float('inf') #Store the minimum number of products can be made with the current inventory level of each part
					for key, value in partDict.items():
						print("partCode, qtyInCode: ", key, value)
						index=partIds.find(key)
						qtyInStock = stock[index]
						productAvail = min(int(qtyInStock/value), productAvail)
						print("productAvail: ", productAvail)					
					
					#Update the inventory					
					productMade = 0
					#Check if productAvail is enough for makeQuantity
					if productAvail >= makeQuantity:
						for key, value in partDict.items():
							index=partIds.find(key)
							stock[index] = stock[index] - makeQuantity*value #stock[index] - makeQuantity*qtyInCode
							print("stock for ", key, stock[index])
						productMade = makeQuantity
						print(f"{productMade} product {makeProduct} successfully made")
						
						#Record the transaction
						fw=open("transactions.txt","a")						
						print(f"make {makeProduct} {productMade}", file=fw)
						fw.close()
						
					else: #The current level of the inventory is insufficient for makeQuantity, calculate outstanding
						for key, value in partDict.items():
							index=partIds.find(key)
							stock[index] = stock[index] - productAvail*value #stock[index] - productAvail*qtyInCode
							print("stock for ", key, stock[index])
						productMade = productAvail
						outstanding = makeQuantity - productMade						
						print(f"{productMade} product {makeProduct} made at the current inventory level.")
						print(f"{outstanding} outstanding.")	
						
						#Record the transaction
						fw=open("transactions.txt","a")						
						print(f"make {makeProduct} {productMade}", file=fw)
						print(f"outstanding {makeProduct} {outstanding}", file=fw)
						fw.close()
			else:
				print(f"Invalid product code {makeProduct} ")

		elif Option == "5": #Get summarised data
			choice = input(f"0-restock, 1-make, 2-outstanding. Enter choice: ")
			if choice == "0": #restock
				with open("transactions.txt", "r") as fr: # no need to close
					data=fr.readlines()
					print("Summarised Data for RESTOCK ***")
					for line in data:
						if line.startswith("restock"):
							lineList = line.split()
							print(f"{lineList[1]}  {lineList[2]}")
			elif choice == "1": #make
				with open("transactions.txt", "r") as fr: # no need to close
					data=fr.readlines()
					print("Summarised Data for MAKE ***")
					for line in data:
						if line.startswith("make"):
							lineList = line.split()
							print(f"{lineList[1]}  {lineList[2]}")
			elif choice == "2": #outstanding
				with open("transactions.txt", "r") as fr: # no need to close
					data=fr.readlines()
					print("Summarised Data for OUTSTANDING ***")
					for line in data:
						if line.startswith("outstanding"):
							lineList = line.split()
							print(f"{lineList[1]}  {lineList[2]}")
			else:
				print("Invalid option.")
		elif Option == "0":
			break
		else:
			print("Invalid input")

TMA2b()
