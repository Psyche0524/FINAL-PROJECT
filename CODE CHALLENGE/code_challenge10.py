
n = 6  

# Top half of the diamond
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        if k % 2 == 0:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()

# Bottom half of the diamond
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        if k % 2 == 0:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()