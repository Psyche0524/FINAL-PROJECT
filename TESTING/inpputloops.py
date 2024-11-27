rows = int(input("Enter rows: "))
columns = int(input("Enter Columns: "))
symbols = input("Enter symbols: ")


for x in range(rows):
    for y in range(columns):
        print(symbols, end= " ")
    print()