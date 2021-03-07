"""
def Q1a():
  Aisle = int(input("Enter number of aisles in supermarket: "))
  FirstAisle = int(input("Enter first aisle: "))
  SecondAisle = int(input("Enter second aisle: "))
  Basket = int((FirstAisle+SecondAisle)/2)
  MinDistance = (Basket-FirstAisle)*2 + (SecondAisle-Basket)*2

  print("The minimum distance is", MinDistance, "units.")

Q1a()
"""
"""
def Q1bi():
  Answer = input("Do you need to go to just one aisle? (yes/no): ")
  if Answer.lower()=="y":
    print("The minimum distance is 0 units")
  else:   
    Aisle = int(input("Enter number of aisles in supermarket: "))
    FirstAisle = int(input("Enter first aisle: "))
    SecondAisle = int(input("Enter second aisle: "))
    Basket = int((FirstAisle+SecondAisle)/2)
    MinDistance = (Basket-FirstAisle)*2 + (SecondAisle-Basket)*2

    print("The minimum distance is", MinDistance, "units.")

Q1bi()
"""
"""
def Q1bii():
  AisleVisit= int(input("Enter the number of aisles to visit: "))
  if AisleVisit==1:
    print("The minimum distance is 0 units")
  elif AisleVisit==2:
    Aisle = int(input("Enter number of aisles in supermarket: "))
    FirstAisle = int(input("Enter first aisle: "))
    SecondAisle = int(input("Enter second aisle: "))
    Basket = int((FirstAisle+SecondAisle)/2)
    MinDistance = (Basket-FirstAisle)*2 + (SecondAisle-Basket)*2
    print("The minimum distance is", MinDistance, "units.")
  else:
    print("Invalid number of aisles for Jane!")

Q1bii()
"""
"""
def Q1ci():
  Supermarket = int(input("Enter number of supermarkets to visit: "))
  for i in range(1,Supermarket+1):
    Aisle = int(input(f'Enter number of aisles in supermarket {i}: '))
    FirstAisle = int(input("Enter first aisle: "))
    SecondAisle = int(input("Enter second aisle: "))
    Basket = int((FirstAisle+SecondAisle)/2)
    MinDistance = (Basket-FirstAisle)*2 + (SecondAisle-Basket)*2

    print("The minimum distance is", MinDistance, "units.")

Q1ci()
"""
def Q1cii():
  Aisle = int(input("Enter number of aisles in supermarket: "))
  MaxAisle = 0
  n=0 # To end the while loop
  AisleList = [] 
  while n<=Aisle:
    AisleVisit = int(input("Enter the aisle number to visit: "))
    n += 1
    if AisleVisit > 0 and AisleVisit <= Aisle: #To prevent error if Aisle is out of range
      AisleList.append(AisleVisit)
      MinAisle = AisleList[0]
      if MaxAisle < AisleVisit: # To ensure MaxAisle is the highest number she visits
        MaxAisle = AisleVisit
      if MinAisle > AisleVisit: # To ensure MinAisle is the lowest number she visists
        MinAisle = AisleVisit
    if AisleVisit == 0 and len(AisleList) == 0:
      print("Not visiting any aisle.")
      break
    elif AisleVisit == 0 and len(AisleList) == 1:
      print("The minimum distance is 0 units")
      break
    elif AisleVisit == 0 and len(AisleList) > 1:
      Basket = int((MaxAisle+MinAisle)/2)
      MinDistance = 0
      for n in range(len(AisleList)):
        if AisleList[n] >  Basket:
         MinDistance += (AisleList[n]-Basket)*2
        else:
          MinDistance += (Basket - AisleList[n])*2
      print(f"The minimum distance is {MinDistance} units.")
      break
Q1cii()