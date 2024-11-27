age = eval(input("Enter your age: "))

if age >= 1 and age <= 7:
	print("That age is categorized as a TODDLER ")
elif age >= 8 and age <= 13:
	print("That age is categorized as a PRE TEEN ")
elif age >= 14 and age <= 18:
	print("That age is categorized as a TEENAGER ")
elif age >= 19 and age <= 31:
	print("That age is categorized as a EARLY ADULTHOOD ")
elif age >= 31 and age <= 45:
	print("That age is categorized as a MID ADULTHOOD ")
elif age >= 46 and age <= 59:
	print("That age is categorized as a POST ADULTHOOD ")
elif age >= 60 and age <= 100:
	print("That age is categorized as a SENIOR ")

else:
	print (" INVALID AGE")