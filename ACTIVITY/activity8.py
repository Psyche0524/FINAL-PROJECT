#GRADING SYSTEM

print("\n\tCHECK YOUR GRADE IF YOU'RE PASSED OR FAILED\n\n")

weights ={
	"prelim":.15,
	"midterm":.15,
	"semifinal":.15,
	"quiz":.25,
	"project":.15,
	"final":.15,
	"tfinal":.70
}

prelim = int(input("Enter your PRELIM Grade: "))
midterm = int(input("Enter your MIDTERM Grade: "))
semifinal = int(input("Enter your SEMI FINAL Grade: "))
quiz = int(input("Enter your QUIZ Grade: "))
project = int(input("Enter your PROJECT Grade: "))
final = int(input("Enter you final Grade: "))
finalgrade = (prelim * weights["prelim"] + midterm * weights["midterm"] +  semifinal * weights["semifinal"] + quiz * weights["quiz"] + project * weights["project"] + final * weights["final"])

if finalgrade > 100:
    print("Invalid input")
elif finalgrade >= 75:
    print(f"You Passed with final grade of {finalgrade}")
else:
    print("You Failed!")