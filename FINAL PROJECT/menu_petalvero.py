print("\t ==================================== \t")
print("\t | WELCOME TO CEEJAY's MENU PROJECT | \t")
print("\t ==================================== \n\t")
print("\n\t Provide the following information to know\n\t")
print("---------------------------------------------------------")

name = input("> Please Enter your First name: ")
section = input("> Enter your Department < \n> BSIT, BSPA, BSE, BSSW, ABELS, BTVTED, DHRS, BSAIS: ")

print("\n\tGREETINGS:\n\t")
print(f"\n\tHello, {name} from {section} WELCOME to my project!\n\t")
print("---------------------------------------------------------")

def main_menu():
    while True:
        print("\n\t\t>>>Python Fundamentals<<<\t")
        print("\n\t     -Main menu- \n")
        print("\t1. Print Statements")
        print("\t2. Variables")
        print("\t3. Operators")
        print("\t4. Conditionals")
        print("\t5. Loops")
        print("\t6. Lists")
        print("\t7. Functions")
        print("\t8. Input and Run your own Python Program")
        print("\t9. Coding Challenge")
        print("\t10. Activities")
        print("\t11. Exit")
        

        choice = input("\n\tEnter the number of your choice: ")
        
        if choice == "1":
            submenu_print_statements()
        elif choice == "2":
            submenu_variables()
        elif choice == "3":
            submenu_operators()
        elif choice == "4":
            submenu_conditionals()
        elif choice == "5":
            submenu_loops()
        elif choice == "6":
            submenu_lists()
        elif choice == "7":
            submenu_functions()
        elif choice == "8":
            run_user_program()
        elif choice == "9":
            submenu_code_challenge()
        elif choice == "10":
            submenu_activities()
        elif choice == "11":
            print("\n\tExiting program. Goodbye!")
            break
        else:
            print("\n\tInvalid choice. Please try again.")

def submenu_print_statements():
    while True:
        print("\n\t     -PRINT STATEMENTS- \n")
        print("\t1. Simple Print Example")
        print("\t2. Formatted Strings")
        print("\t3. Back to Main Menu")

        choice = input("\n\tEnter your choice:")

        if choice == "1":
            print("\nInput: \n\tname = input('Enter your name: ') \n\tage = int(input('Enter your age:')\n\tprint(f'Hello {name}, you are {age} years old!')")
            print("\nOutput: \n\tEnter your name: John \n\tEnter your age: 25")
            print("\nTRY THE PROGRAM\n")
            from ex_print_statement import name
        elif choice == "2":
            print("\nInput: \n\tname = input('Please Enter your name: ') \n\tprint(f'Hello, {name}!')\n")
            print("\nOutput: \n\tHello, John! (if name = 'John')")
            print("\nTRY THE PROGRAM\n")
            from ex_Formatted_Strings import name
        elif choice == "3":
            break
        else:
            print("\n\tInvalid choice. Please try again.")

def submenu_variables():
    while True:
        print("\n\t     -VARIABLES- \n")
        print("\t1. Declaring Variables")
        print("\t2. Updating Variables")
        print("\t3. Back to Main Menu")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            print("\nInput: \n\tname = 'John' \n\tage = 25 \n\tprint(f'Name: {name}, Age: {age}')")
            print("\nOutput: \n\tName: John, Age: 25")
        elif choice == "2":
            print("\nInput: \n\tage = 26  # updating the age \n\tprint(f'Updated age: {age}')")
            print("\nOutput: \n\tUpdated age: 26")
        elif choice == "3":
            break
        else:
            print("\n\tInvalid choice. Please try again.")

def submenu_operators():
    while True:
        print("\n\t     -OPERATORS- \n")
        print("\t1. Arithmetic Operators")
        print("\t2. Comparison Operators")
        print("\t3. Back to Main Menu")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            print("\nInput: \n\tnum1 = int(input('Enter the first number: ')) \n\tnum2 = int(input('Enter the second number: ')) \n\tsubtraction = num1 - num2\n\tmultiplication = num1 * num2\n\tdivision = num1 / num2\n \n\tprint(f'Addition: {addition}, Subtraction: {subtraction}, Multiplication: {multiplication}, Division: {division}')\n")
            print("\nOutput: \n\tEnter the first number: 10 \n\tEnter the second number: 5 \n\tAddition: 15, Subtraction: 5, Multiplication: 50, Division: 2.0\n")
            print("\nTRY THE PROGRAM\n")
            from activity4 import num1
        elif choice == "2":
            print("\nInput: \n\ta = 10 \n\tb = 20 \n\tprint(a == b)  # equal to \n\tprint(a != b)  # not equal to \n\tprint(a > b)   # greater than \n\tprint(a < b)   # less than \n\tprint(a >= b)  # greater than or equal to \n\tprint(a <= b)  # less than or equal to ")
            print("\nOuput: \n\tFalse \n\tTrue \n\tFalse \n\tTrue \n\tFalse \n\tTrue")
        elif choice == "3":
            break
        else:
            print("\n\tInvalid choice. Please try again.")

# Implement the remaining submenus in a similar way...

def submenu_conditionals():
    while True:
        print("\n\t     -CONDITIONALS- \n")
        print("\t1. If Statements")
        print("\t2. If-Else Statements")
        print("\t3. Back to Main Menu")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            print("\nInput:\n\tage = int(input('Enter your age: ')) \n\tif age >= 18: \n\tprint('You are an adult.')")
            print("\nOutput:\n\tEnter your age: 20 \n\tYou are an adult.")
            print("\nTRY THE PROGRAM\n")
            from ex_ifstatements import age
        elif choice == "2":
            print("\nInput:\n\tuser = input('ENTER NAME : ') \n\tage = eval(input('ENTER AGE : ')\n \nif age >= 1 and age <= 7:        \n\tprint(f'Hi {user}, you are toddler.') \nelif age >= 8 and age <= 13:      \n\tprint(f'Hi {user}, you are pre teen.') \nelif age >= 14 and age <= 18:        \n\tprint(f'Hi {user}, you are teenager.') \nelif age >= 19 and age <= 31:        \n\tprint(f'Hi {user}, you are early adulthood.') \nelif age >= 32 and age <= 45:     \n\tprint(f'Hi {user}, you are mid adulthood.') \nelif age >= 46 and age <= 59:       \n\tprint(f'Hi {user}, you are port adulthood.') \nelif age >= 60 and age <= 100:     \n\tprint(f'Hi {user}, you are senior.') \nelse:      \n\tprint(f'Impossible Your Alive, {user}!')")
            print("\nOutput: \n\tENTER NAME : Ceejay \n\tENTER AGE : 18 \n\tHi Ceejay, you are teenager.")
            print("\nTRY THE PROGRAM\n")
            from activity9 import age
        elif choice == "3":
            break
        else:
            print("\n\tInvalid choice. Please try again.")

def submenu_loops():
    while True:
        print("\n\t     -LOOPS- \n")
        print("\t1. For Loop")
        print("\t2. While Loop")
        print("\t3. Back to Main Menu")

        choice = input("\t\nEnter your choice: ")

        if choice == "1":
            print("\nInput: \nfor u in range(1, 6): \n\tprint('  ' * u, end=' ') \nfor x in range(u, 6): \n\tprint('*', end=' ') \nprint() ")
            print("\nOutput:")
            from code_challenge9 import u
        elif choice == "2":
            print("\nInput:\ntotal_sum = 0 \nwhile True: \n\tnumber = int(input('Enter a number: ')) \n\tif number == 0: \n\t\tprint('Loop has terminated') \n\t\tbreak \n\ttotal_sum += number \nprint(f'The sum of all the numbers given is {total_sum}'")
            print("\nOutput: \n\tEnter a number: 1\n\tEnter a number: 2\n\tEnter a number: 3\n\tEnter a number: 4\n\tEnter a number: 5\n\tEnter a number: 6\n\tEnter a number: 8\n\tEnter a number: 9\n\tEnter a number: 0\n\tLoop has terminated\n\tThe sum of all the numbers given is 45")
            print("\nTRY THE PROGRAM: \n")
            from code_challenge14 import total_sum
        elif choice == "3":
            break
        else:
            print("\n\tInvalid choice. Please try again.")

def submenu_lists():
    while True:
        print("\n\t     -LISTS- \n")
        print("\t 1. Creating a List")
        print("\t 2. Accessing List Elements")
        print("\t 3. Back to Main Menu")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            print("\nInput: \n\tcourses = ['BSIT', 'BSA', 'BSAIS', 'BTVTED', 'BSSW', 'BSPA', 'Delete w/o index', 'Delete with index'] \n\n\tcourses.remove('Delete w/o index') \n\tcourses.pop() \n\tcourses.append('DHRS') \n\tcourses.insert(0, 'ABELS') \n\nprint(courses)")
            print("\nOutput: \n\t['ABELS', 'BSIT', 'BSA', 'BSAIS', 'BTVTED', 'BSSW', 'BSPA', 'DHRS']")
        elif choice == "2":
            print("\nInput: \n\tfruits = ['apple', 'banana', 'cherry'] \n\tprint(f'First fruit: {fruits[0]}')  # Accessing the first item \n\tprint(f'Second fruit: {fruits[1]}')  # Accessing the second item")
            print("\nOutput: \n\tFirst fruit: apple \n\tSecond fruit: banana")
        elif choice == "3":
            break
        else:
            print("\n\tInvalid choice. Please try again.")

def submenu_functions():
    while True:
        print("\n\t     -FUNCTIONS- \n")
        print("\t1. Defining a Function")
        print("\t2. Calling a Function")
        print("\t3. Back to Main Menu")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            print("\nInput: \n\task = input('Please Enter your pangalan: '') \n\tprint(f'Hello, my name is {ask}')\n \n\tdef greet(name):  \n\t\treturn f'Hi my name is, {name}!' \n\tprint(greet('Alice'))")
            print("\nOutput: \n\tHello, my name is User \n\tHi my name is, Alice!")
            print("\nTRY THE PROGRAM\n")
            from ex_deffuntion import ask
        elif choice == "2":
            print("\nInput:\ndef add_numbers(a, b):  \n\treturn a + b  \nresult = add_numbers(3, 5) \nprint(f'Sum: {result}')")
            print("\nOutput: \n\tSum: 8")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
def run_user_program():
    
    """Allows the user to input and run their Python code."""
    
    print("\n--- Run Your Own Python Program ---")
    print("Type your Python code below. To finish, enter a blank line.")
    user_code = []
    while True:
        line = input()
        if line.strip() == "":
            break
        user_code.append(line)
    try:
        exec("\n".join(user_code))
    except Exception as e:
        print(f"Error executing your code: {e}")
    input("Press Enter to return to the main menu...\n")

def submenu_code_challenge():
    while True:
        print("\n\t\t=== CODE CHALLENGE ===\t\n")
        print("\tPICK A NUMBER FROM THE OPTIONS BELOW")
        print("\n\t1. CODE CHALLENGE 1")
        print("\t2. CODE CHALLENGE 2")
        print("\t3. CODE CHALLENGE 3")
        print("\t4. CODE CHALLENGE 4")
        print("\t5. CODE CHALLENGE 5")
        print("\t6. CODE CHALLENGE 6")
        print("\t7. CODE CHALLENGE 7")
        print("\t8. CODE CHALLENGE 8")
        print("\t9. CODE CHALLENGE 9")
        print("\t10. CODE CHALLENGE 10")
        print("\t11. CODE CHALLENGE 11")
        print("\t12. CODE CHALLENGE 12")
        print("\t13. CODE CHALLENGE 13")
        print("\t14. CODE CHALLENGE 14")
        print("\t15. CODE CHALLENGE 15")
        print("\t16. CODE CHALLENGE 16")
        print("\t17. EXIT TO MAIN MENU")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            print("\n\tCODE CHALLENGE 1\n")
            from code_challenge1 import asterisk
        elif choice == "2":
            print("\n\tCODE CHALLENGE 2\n")
            from code_challenge2 import name
        elif choice == "3":
            print("\n\tCODE CHALLENGE 3\n")
            pass
        elif choice == "4":
            print("\n\tCODE CHALLENGE 4\n")
            from code_challenge5 import ask1
        elif choice == "6":
            print("\n\tCODE CHALLENGE 6\n")
            from code_challenge6 import FG
        elif choice == "7":
            print("\n\tCODE CHALLENGE 7\n")
            from code_challenge7 import age
        elif choice == "8":
            print("\n\tCODE CHALLENGE 8\n")
            from code_challenge8 import sum
        elif choice == "9":
            print("\n\tCODE CHALLENGE 9\n")
            from code_challenge9 import u
        elif choice == "10":
            print("\n\tCODE CHALLENGE 10\n")
            from code_challenge10 import x
        elif choice == "11":
            print("\n\tCODE CHALLENGE 11\n")
            from code_challenge11 import x
        elif choice == "12":
            print("\n\tCODE CHALLENGE 12\n")
            from code_challenge12 import x
        elif choice == "13":
            print("\n\tCODE CHALLENGE 13\n")
            from code_challenge13 import i
        elif choice == "14":
            print("\n\tCODE CHALLENGE 14\n")
            from code_challenge14 import total_sum
        elif choice == "15":
            print("\n\tCODE CHALLENGE 15\n")
            from code_challenge15 import word
        elif choice == "16":
            print("\n\tCODE CHALLENGE 16\n")
            from code_challenge16 import user
        elif choice == "17":
            print("\n\tReturning to main menu...\n")
            break
        else:
            print("\n\tInvalid choice. Please choose again.")
def submenu_activities():
    while True:
        print("\n\t\t=== ACTIVITIES ===\t\n")
        print("\tPICK A NUMBER FROM THE OPTIONS BELOW")
        print("\n\t1. FLOOR DIVISION")
        print("\t2. BIO DATA")
        print("\t3. THE SUM OF")
        print("\t4. FAHRENHEIT")
        print("\t5. BREAKDOWN")
        print("\t6. GOLD")
        print("\t7. PASSWORD")
        print("\t8. AGE CATEGORIZED")
        print("\t9. FRESHMEN TO SENIOR")
        print("\t10. CIRCLE")
        print("\t11. STOPPING POINT")
        print("\t12. FOR LOOP WITH RANGE")
        print("\t13. FOR LOOP COMPLETE RANGE")
        print("\t14. FOR LOOP WITH RANGE v2")
        print("\t15. FOR LOOP WITH RANGE v3")
        print("\t16. COLUMNS")
        print("\t17. TRIANGLE")
        print("\t18. WHILE LOOP")
        print("\t19. CREATE MORE TRIANGLE")
        print("\t20. LOOP")
        print("\t21. FUNCTION")
        print("\t22. RETURN")
        print("\t23. IMPORTING")
        print("\t24. LIST")
        print("\t25. EXIT TO MAIN MENU")


        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            print("\n\tFLOOR DIVISION\n")
            from activity2 import ask
        elif choice == "2":
            print("\n\tBIO DATA\n")
            from activity3 import experience
        elif choice == "3":
            print("\n\tTHE SUM OF\n")
            from activity4 import num1
        elif choice == "4":
            print("\n\tFAHRENHEIT\n")
            from activity5 import temp
        elif choice == "5":
            print("\n\tBREAKDOWN\n")
            from activity6 import num
        elif choice == "6":
            print("\n\tGOLD\n")
            from activity7 import gold
        elif choice == "7":
            print("\n\tPASSWORD\n")
            from activity8 import password
        elif choice == "8":
            print("\n\tAGE CATEGORIZED\n")
            from activity9 import user
        elif choice == "9":
            print("\n\tFRESHMEN TO SENIOR\n")
            from activity10 import name
        elif choice == "10":
            print("\n\tCIRCLE\n")
            from activity11 import circle
        elif choice == "11":
            print("\n\tSTOPPING POINT\n")
            from activity12 import food
        elif choice == "12":
            print("\n\tFOR LOOP WITH RANGE\n")
            from activity13 import factorial
        elif choice == "13":
            print("\n\tFOR LOOP COMPLETE RANGE\n")
            from activity14 import i
        elif choice == "14":
            print("\n\tFOR LOOP WITH RANGE v2\n")
            from activity15 import y
        elif choice == "15":
            print("\n\tFOR LOOP WITH RANGE v3\n")
            from activity16 import i
        elif choice == "16":
            print("\n\tCOLUMNS\n")
            from activity17 import columns
        elif choice == "17":
            print("\n\tTRIANGLE\n")
            from activity18 import triangles
        elif choice == "18":
            print("\n\tWHILE LOOP\n")
            from activity19 import con
        elif choice == "19":
            print("\n\tCREATE MORE TRIANGLE\n")
            from activity20 import isContinue
        elif choice == "20":
            print("\n\tLOOP\n")
            from activity21 import go
        elif choice == "21":
            print("\n\tFUNCTION\n")
            from activity22 import temp
        elif choice == "22":
            print("\n\tRETURN\n")
            from activity23 import temp
        elif choice == "23":
            print("\n\tIMPORTING\n")
            from activity24 import temp
        elif choice == "24":
            print("\n\tLIST\n")
            from activity25 import courses
        elif choice == "25":
            print("\n\tReturning to main menu...\n")
            break
        else:
            print("\n\tInvalid choice. Please try again.\n")
# Run the program
main_menu()