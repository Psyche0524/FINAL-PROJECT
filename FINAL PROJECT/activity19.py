con = True

while con == True:
    name = input("Enter a name: ")
        
    if name.lower() == "stop":
        print("The loop has been Terminated")
            
        break
        con = False