word = True
count = 0

while word == True:
    ask = input(" Please Enter a words: ")

    if ask.lower() == "stop":
        print("Loop has now stopped")
        break
        word = False
    else:
        count += 1 
        continue

