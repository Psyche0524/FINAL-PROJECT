word = True
count = 0
no = 0
while word:
    ask = input(" Do you want to create a new triangle (yes or no): -- >")

    if ask.lower() == "no" :
        print("Loop has now stopped")
        break
    elif ask.lower() == "yes":
        no += 1 
        for x in range(1,6):
            for r in range(1,no + 1):
                for y in range(1,x+1):
                    print("*", end=" ")
                for z in range(6, x, -1):
                    print(" ", end=" ")
            print()
        continue 
    else:
        print("Invalid answer, please only answer 'yes' or 'no' ")
        continue       