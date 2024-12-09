def act5():
    temp = int(input("Enter temperature in farenheit: "))
    cel = (temp - 32) * 5/9
    round = (round(cel, 2))
    print(f"The conversion of {temp} degrees farenheit is {round}")