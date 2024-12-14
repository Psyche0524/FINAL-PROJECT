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
        print("\t9. Exit")

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
            print("\nTRY THE PROGRAM\n")
            from ex_decvariables import name
        elif choice == "2":
            print("\nInput: \n\tage = 26  # updating the age \n\tprint(f'Updated age: {age}')")
            print("\nOutput: \n\tUpdated age: 26")
            from ex_upvariables import age
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
            print("\nInput:\n\tage = int(input('Enter your age: ')) \n\tif age >= 18:  \n\tprint('You are an adult.') \nelse: \n\tprint('You are a minor.')")
            print("\nOutput: \n\tEnter your age: 16 \n\tYou are a minor.")
            print("\nTRY THE PROGRAM\n")
            from ex_ifelsestatements import age
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
            print("\nInput: \n\tfor i in range(3):  \n\tprint(f'Iteration {i}')")
            print("\nOutput: \n\tIteration 0 \n\tIteration 1 \n\tIteration 2")
            from ex_forloop import i
        elif choice == "2":
            print("\nExample:\n\tcounter = 0 \n\twhile counter < 3:  \n\tprint(f'Counter: {counter}') \n\tcounter += 1")
            print("\nOutput: \n\tCounter: 0 \n\tCounter: 1 \n\tCounter: 2")
            from ex_whileloop import counter
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
            print("\nInput: \n\tfruits = ['apple', 'banana', 'cherry'] \n\tprint(f'List of fruits: {fruits}')")
            print("\nOutput: \n\tList of fruits: ['apple', 'banana', 'cherry']")
            from ex_List import fruits
        elif choice == "2":
            print("\nInput: \n\tfruits = ['apple', 'banana', 'cherry'] \n\tprint(f'First fruit: {fruits[0]}')  # Accessing the first item \n\tprint(f'Second fruit: {fruits[1]}')  # Accessing the second item")
            print("\nOutput: \n\tFirst fruit: apple \n\tSecond fruit: banana")
            from ex_List import fruits
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
            print("\nInput: \n\task = input('Please Enter your pangalan: '') \n\tprint(f'Hello, my name is {ask}') \n\tdef greet(name):  \n\treturn f'Hi my name is, {name}!' \n\tprint(greet('Alice'))")
            print("\nOutput: \n\tHello, my name is User \n\tHi my name is, Alice!")
            print("\nTRY THE PROGRAM\n")
            from ex_deffuntion import ask
        elif choice == "2":
            print("\nInput:\n\tdef add_numbers(a, b):  \n\treturn a + b  \n\tresult = add_numbers(3, 5) \n\tprint(f'Sum: {result}')")
            print("\nOutput: \n\tSum: 8")
            print("\nTRY THE PROGRAM\n")
            from ex_Callfunction import result
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

# Run the program
main_menu()