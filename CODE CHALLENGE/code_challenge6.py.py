#GRADING SYSTEM

print("\n\tCHECK YOUR GRADE IF YOU'RE PASSED OR FAILED\n\n")

prelim = eval(input("ENTER YOU PRELIM GRADE : "))
midterm = eval(input("ENTER YOU MIDTERM GRADE : " ))
sfinals = eval(input("ENTER YOU SEMI FINALS GRADE : "))
finals = eval(input("ENTER YOU FINALS GRADE : " ))
quiz = eval(input("ENTER YOU QUIZ GRADE : "))
project = eval(input("ENTER YOU PROJECT GRADE : "))

if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <=100) and (sfinals >= 65 and sfinals <= 100) and (finals >= 65 and finals <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
	fg = (prelim * 0.15) + (midterm * 0.15) + (sfinals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)
	#nested condition 
	if fg >=75:
		print("Congratulations, Homies you passed the course!")
	else:
		print("Sorry, Pare you failed bawe ka nalang sa susunod!")


else:
	print("INVALID GRADES")