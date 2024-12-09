def act21():
    go = True
    count = 0

    while go == True:
        name = input("Please enter a name ---> ")
        
        if name.lower() == "stop":
            print("Loop has now stopped")
            print(f"You have entered {count} number")
            break
            go = False
        else:
            count += 1