isBuy = input("Did you buy a grocery?: (yes or no): ")

if isBuy.lower() == "yes":

	name = input("Enter your name: ")
	nameItem = input("Name of Item: ")
	priceItem = float(input("Price of the Item: "))
	age = eval(input("Age:"))
	givenAmount = eval(input("Amount Given:"))

discount = round((priceItem * 0.052), 2)
discountPrice = round((priceItem - discount), 2)
tax = round((priceItem * 0.123), 2)
taxPrice = round((priceItem + tax), 2)

if age >= 60:

	print(f"\nHi {name}, you purchased a {nameItem}, with a price of {priceItem}PHP plus a 5.2% discount ({discount}PHP) to your total purchased. ")
	print(f"Total of : {round((priceItem - discount), 2)}")
	print(f"Change : {round((givenAmount - discountPrice), 2)}")
	print(f"thank you for buying, Please come again next time. " )

elif age >= 18:

	print(f"Hi {name}, you purchased a {nameItem}, with a price of {priceItem}PHP plus a 5.2% discount ({discount}PHP) to your total purchased. ")	
	print(f"Total of : {round((priceItem + tax), 2)}")
	print(f"Change : {round((givenAmount - taxPrice), 2)}")
	print(f"thank you for buying, Please come again next time. " )

else:
	print("Thank you for Looking, Please come again next time. " )