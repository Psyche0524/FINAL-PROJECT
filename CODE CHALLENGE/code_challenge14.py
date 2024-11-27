total_sum = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print("Loop has terminated")
        break
    total_sum += number

print(f"The sum of all the numbers given is {total_sum}")
