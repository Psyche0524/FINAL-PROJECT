#introduction to conditional statements

gold = 0
miner = input ("Hi, what is your name : ")

isGold = input("is the mineral gold? ")

if isGold.lower() == "yes":
	gold += 1
	print(f"Hi {miner}, Your total number of gold is {gold}")
else:
	print(f"Hi {miner}, Your total number of gold is {gold}")