# FAHRENHEIT TO CELSIUS CONVERTER
ask1 = input("HELLO YOU WANT TO PRINT THIS PROGRAM?\nHIT THE ENTER BUTTON TO RUN")

print("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM")

print("=========================================")

fahrenheit = eval(input("Enter temperature in Fahrenheit ---> : "))
celsius = ((fahrenheit - 32) * 5 / 9)

print(f"{fahrenheit} °F converted to celsius is {round(celsius, 2)} °C.")