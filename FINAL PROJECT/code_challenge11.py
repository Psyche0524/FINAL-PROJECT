# Arrow up
for x in range(1, 5):
    for y in range(5, x, -1):
        print("   ", end=" ")
    for u in range(1, x + 1):
        print("  *", end=" ")
    for o in range(1, x):
        print("  *", end=" ")
    print()

# Arrow down
for x in range(3, 0, -1):
    for y in range(5, x, -1):
        print("   ", end=" ")
    for u in range(1, x + 1):
        print("  *", end=" ")
    for o in range(1, x):
        print("  *", end=" ")
    print()






