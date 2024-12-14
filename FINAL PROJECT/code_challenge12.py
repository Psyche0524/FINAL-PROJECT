#Arrow up!
for x in range(1,6):
    for y in range(6, x, -1):
        print(" ", end= " ")
    for u in range(1, x+1):
        print("*", end= " ")
    for o in range(1, x+1):
        print("*", end= " ")
    print()
#Arrow Down!
for a in range(1,7):
    for b in range(1, x + 1):
        print (" ", end= " ")
    
    for a in range(7, x, -1):
        print("*", end= " ")

    for a in range(4,x, -1):
        print(x, end=" ")
    print( )


