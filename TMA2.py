def getPartsInCode(productCode):
  partIds = "ABCDEFGHIJKL"
  format = ""
  for n in range(len(productCode)):
    if productCode[n] in partIds:
      if productCode[n] == 0 or productCode[n] != productCode[n-1]:
        format+= str(productCode.count(productCode[n])) + productCode[n] + " "
  return format

def validateInput(newProductCode, partIds):
  codeWithUniqueParts = set(newProductCode)

  if len(codeWithUniqueParts) > 3:
    return "invalid"
  else:
    if len(newProductCode)<3:    
      return "invalid"
    else:
      #Check if each character is a letter from A to L.
      for c in newProductCode:
        if c not in partIds:        
          return "invalid"
      else: #Iterated through all characters in newProductCode, all chars are valid, newProductCode is valid
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
    Option = int(input("Select Menu Option: "))
    if Option == 1: #Add product code      
      productCode = str(input("Enter new product code: ").upper())
      ''.join(sorted(productCode)) #To sort product code alphabetically
      #Validate the input
      if validateInput(productCode) == "invalid":
        print("The product code is invalid")
      elif productCode.upper() in productCodes:      
          print("The product code already exist")
      else:
        productCodes.append(productCode.upper())
        print("The product code has been added successfully")

    elif Option == 2: #List inventory
      print('Part Stock Level')
      for n in range(len(partIds)):
        print(f'{partIds[n]:3s} {stock[n]:5d}', end='')
        if stock[n] <= reorderPoint:
          print('  ***')
        else:
          print()

    elif Option == 3: #Update inventory
      updated = []
      while True:
        identifier = input("Enter part identifier or <ENTER> to end: ")
        if identifier not in partIds:
          print("The part identifier is invalid")      
        elif identifier == "":
          return      
        else:
          index=partIds.find(identifier)
          print(f"Current stock level for {identifier} = {stock[index]}")
          quantity = int(input("Enter quantity to add: "))
          if not quantity.is_integer() and quantity <= 0:
            print("The quantity is invalid")
          else:
            stock[index] += quantity
            print(f"Updated stock level for {identifier} = {stock[index]}")
            updated.append([identifier,quantity])
      fw=open("transactions.txt","w")
      for identifier,quantity in updated:
          print(f"restock {identifier} {quantity}", file=fw)
      fw.close()

    elif Option == 4: #Make Product
      makeProduct = str(input(f"Enter product code: "))
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
          spaceIndex = 0 #Store the index of the last space iterated
          partCode = ""
          qtyInCode = 0
          for n in len(qtyAndPartStr):
            if qtyAndPartStr[n].isalpha(): #Get the part code
              partCode = qtyAndPartStr[n]
              qtyInCode = int(qtyAndPartStr[spaceIndex+1:n])              
              partDict[partCode] = qtyInCode 
          lastPart_totalQty = qtyInCode*makeProduct
          lastPart_code = partCode
          index = partIds.find(lastPart_code)          
          lastPart_originalStock = stock[index]

          #Check the stock
          minBalance = float('inf') #Store the minimum balance
          for key, value in partDict.items():
            index=partIds.find(key)
            qtyInStock = stock[index]
            minBalance = min((qtyInStock - value*makeQuantity), minBalance)
          
          #Update the inventory
          for key, value in partDict.items():
            index=partIds.find(key)
            stock[index] = stock[index] - value*makeQuantity #stock[index] - qtyIncode*makeQuantity
            if minBalance < 0: #If the balance is negative => insufficient inventory, update all parts following the current inventory level
              stock[index] = stock[index] - minBalance
          
          #Get outstanding products
          if minBalance < 0:
            index = partIds.find(lastPart_code)  
            #curstock = oriStock - totalQty
            #supposed_totalQty = qtyincode * makeProduct
            #actual_totalQty = qtyincode * makeProduct - qtyincode*outstanding          
            #supposed_totalqty - actual_totalQty = qtyincode*outstanding
            

          
          print(f"{makeQuantity} product {makeProduct} successfully made")
      else:
        print(f"Invalid product code {makeProduct} ")

    elif Option == 5: #Get summarised data
      summaryData = int(input(f"0-restock, 1-make, 2-outstanding. Enter choice: "))
      if summaryData == 0:
        with open("transactions.txt", "r") as fr: # no need to close
          data=fr.read()
        print(data)
      elif summaryData == 1:
        pass
      else:
        pass
    elif Option == 0:
      break
    else:
      print("Invalid input")

TMA2b()
