
print("-------------------- PASSED OR FAILED PROGRAM -------------------")
print(input("Press enter to start the program."))

print("Provide the following information to know if you pass or fail.")
user = input("PLEASE INPUT YOUR NAME : ")

#variables
prelim = eval(input("PRELIMINARY GRADE      : ")) * 0.15
midterm = eval(input("MIDTERM GRADE          : ")) * 0.15
semiFinal = eval(input("SEMI-FINAL GRADE       : ")) * 0.15
final = eval(input("FINAL GRADE            : ")) * 0.15
quiz = eval(input("QUIZ GRADE             : ")) * 0.25
project = eval(input("PROJECT GRADE          : ")) * 0.15

FG = prelim + midterm + semiFinal + final + quiz + project      #formula

print("__________________________________________________________________")
#conditions
if FG > 98:
    print("Invalid Grade, please try again.")
elif FG >= 75:
    print(f"You're Passed with a grade of {FG}, Congratulations {user}.")
    print("Thank you for using the program.")
else:
    print(f"You Failed with a grade of {FG}, Better luck next time {user}.")
    print("Thank you for using the program.")