name = input("Enter a name: ")
number = eval(input ("Enter a number: "))

if number % 9 == 5 and number % 5 == 0:
    print(f" Hi {name}, the number you just entered is an ODD number and {number} divisible by to 5 or 9")
elif number % 5 == 0:
    print(f" Hi {name}, the number you just entered is an ODD number, but {number} is not divisible by to 5 but divisible by 9")
elif number % 5 == 0:
    print(f" Hi {name}, the number you just entered is an ODD number, but {number} is not divisible by to 9 divisible but 5'")
elif number % 2 == 0:
    print(f" Hi {name}, the number you just entered is an EVEN but {number} is not divisible by 9 or 5")
else:
    print(f" Hi {name}, the number you just entered is an ODD number but {number} is not divisible by 5 or 9")