print("\t ==================================== \t")
print("\t | WELCOME TO CEEJAY's MENU PROJECT | \t")
print("\t ==================================== \n\t")
print("\n\t Please Enter your name and Department\n\t")
print("-------------------------------------------------------------")
name = input("> Please Enter your First name: ")
section = input("> Enter your Department < \n> BSIT, BSPA, BSE, BSSW, ABELS, BTVTED, DHRS, BSAIS: ")
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")
print("\n\tGREETINGS:\n\t")
print(f"\n\tHello, {name} from {section} WELCOME to my project!\n\t")
print("-------------------------------------------------------------")

def main_menu():
    while True:
        print("\n\t\t>>>Python Fundamentals<<<\t")
        print("\n\t  -Main Menu-\n\t")
        print("\t1. Print Statements")
        print("\t2. Variables")
        print("\t3. Operators")
        print("\t4. Conditionals")
        print("\t5. Loops")
        print("\t6. Lists")
        print("\t7. Functions")
        print("\t8. Coding Challenge")
        print("\t9. Activities")
        print("\t10. Exit")

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
            submenu_codechallenge()
        elif choice == "9":
            submenu_activities()
        elif choice == "10":
            print("\n\tExiting program. Goodbye!")
            break
        else:
            print("\n\tInvalid choice. Please try again.")

def submenu_print_statements():
    while True:
        print("\n\t=== Print Statements ===")
        print("\t1. Simple Print Example")
        print("\t2. Formatted Strings")
        print("\t3. Back to Main Menu")

        choice = input("\n\tEnter your choice: ")

        if choice == "1":
            print("\n\tExample: \n\tprint('Hello, World!')")
            print("\n\tOutput: \n\tHello, World!")
        elif choice == "2":
            print("\n\tExample: \n\tprint(f'Hello, {name}!')\n")
            print("\n\tOutput: \n\tHello, John! (if name = 'John')")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def submenu_variables():
    while True:
        print("\n=== Variables Submenu ===")
        print("1. Declaring Variables")
        print("2. Updating Variables")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Example: x = 5")
            print("Variable x is assigned the value 5.")
        elif choice == "2":
            print("Example: x = 5; x = x + 3")
            print("Variable x now holds the value 8.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def submenu_operators():
    while True:
        print("\n=== Operators Submenu ===")
        print("1. Arithmetic Operators")
        print("2. Comparison Operators")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Example: 5 + 3 = 8")
        elif choice == "2":
            print("Example: 5 > 3 is True")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Implement the remaining submenus in a similar way...

def submenu_conditionals():
    while True:
        print("\n=== Conditionals Submenu ===")
        print("1. If Statements")
        print("2. If-Else Statements")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Example:\nif x > 0:\n    print('Positive')")
        elif choice == "2":
            print("Example:\nif x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def submenu_loops():
    while True:
        print("\n=== Loops Submenu ===")
        print("1. For Loop")
        print("2. While Loop")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Example:\nfor i in range(5):\n    print(i)")
        elif choice == "2":
            print("Example:\ni = 0\nwhile i < 5:\n    print(i)\n    i += 1")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def submenu_lists():
    while True:
        print("\n=== Lists Submenu ===")
        print("1. Creating a List")
        print("2. Accessing List Elements")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Example: my_list = [1, 2, 3]")
        elif choice == "2":
            print("Example: my_list[0] returns 1 (first element of the list)")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def submenu_functions():
    while True:
        print("\n=== Functions Submenu ===")
        print("1. Defining a Function")
        print("2. Calling a Function")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Example:\ndef greet():\n    print('Hello!')")
        elif choice == "2":
            print("Example:\ndef greet():\n    print('Hello!')\ngreet()")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
def submenu_codechallenge():
    while True:
        print("\n === Code Challenge ===")
        print("\tPICK A NUMBER FROM THE OPTIONS BELOW")
        print("\n1. CODE CHALLENGE 1")
        print("2. CODE CHALLENGE 2")
        print("3. CODE CHALLENGE 3")
        print("4. CODE CHALLENGE 4")
        print("5. CODE CHALLENGE 5")
        print("6. CODE CHALLENGE 6")
        print("7. CODE CHALLENGE 7")
        print("8. CODE CHALLENGE 8")
        print("9. CODE CHALLENGE 9")
        print("10. CODE CHALLENGE 10")
        print("11. CODE CHALLENGE 11")
        print("12. CODE CHALLENGE 12")
        print("13. CODE CHALLENGE 13")
        print("14. CODE CHALLENGE 14")
        print("15. CODE CHALLENGE 15")
        print("16. CODE CHALLENGE 16")
        print("17. EXIT TO MAIN MENU")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("CODE CHALLENGE 1")
            from code_challenge1 import asterisk
        elif choice == "2":
            print("CODE CHALLENGE 2")
            from code_challenge2 import name
        elif choice == "3":
            print("CODE CHALLENGE 3")
            pass
        elif choice == "4":
            print("CODE CHALLENGE 4")
            from code_challenge4 import ask
        elif choice == "5":
            print("CODE CHALLENGE 5")
            from code_challenge5 import ask1
        elif choice == "6":
            print("CODE CHALLENGE 6")
            import code_challenge6
            code_challenge6.run_challenge6()
        elif choice == "7":
            print("CODE CHALLENGE 7")
            import code_challenge7
            code_challenge7.run_challenge7()
        elif choice == "8":
            print("CODE CHALLENGE 8")
            import code_challenge8
            code_challenge8.run_challenge8()
        elif choice == "9":
            print("CODE CHALLENGE 9")
            import code_challenge9
            code_challenge9.run_challenge9()
        elif choice == "10":
            print("CODE CHALLENGE 10")
            import code_challenge10
            code_challenge10.run_challenge10()
        elif choice == "11":
            print("CODE CHALLENGE 11")
            import code_challenge11
            code_challenge11.run_challenge11()
        elif choice == "12":
            print("CODE CHALLENGE 12")
            import code_challenge12
            code_challenge12.run_challenge12()
        elif choice == "13":
            print("CODE CHALLENGE 13")
            import code_challenge13
            code_challenge13.run_challenge13()
        elif choice == "14":
            print("CODE CHALLENGE 14")
            import code_challenge14
            code_challenge14.run_challenge14()
        elif choice == "15":
            print("CODE CHALLENGE 15")
            import code_challenge15
            code_challenge15.run_challenge15()
        elif choice == "16":
            print("CODE CHALLENGE 16")
            import code_challenge16
            code_challenge16.run_challenge16()
        elif choice == "17":
            print("Returning to main menu...")
        else:
            print("Invalid choice. Please choose again.")
def submenu_activities():
    while True:
        print("\n === ACTIVITIES ===")
        print("\n\tWELCOME TO ACTIVITY FOLDER.")
        print("\t=====================================")
        print("\tPICK A NUMBER FROM THE OPTIONS BELOW")
        print("\n1. GRADING SYSTEM")
        print("2. STOP THE LOOP!")
        print("3. CREATE MORE TRIANGLE")
        print("4. AGE CATEGORIZED")
        print("5. AGE CATEGORIZED v2")
        print("6. GROCERY SYSTEM")
        print("7. SUMMATION")
        print("8. TRIANGLE")
        print("9. DIAMOND v2")
        print("10. DIAMOND")
        print("11. ARROW UP")
        print("12. DIAMOND NUMBERS 1 to 5")
        print("13. The Sum of all numbers given")
        print("14. CREATE MORE TRIANGLE")
        print("15. BANK SIMULATION PROGRAM")
        print("16. ADDITIONAL ACTIVITY 1")
        print("17. ADDITIONAL ACTIVITY 2")
        print("18. ADDITIONAL ACTIVITY 3")
        print("19. ADDITIONAL ACTIVITY 4")
        print("20. ADDITIONAL ACTIVITY 5")
        print("21. ADDITIONAL ACTIVITY 6")
        print("22. ADDITIONAL ACTIVITY 7")
        print("23. ADDITIONAL ACTIVITY 8")
        print("24. ADDITIONAL ACTIVITY 9")
        print("25. EXIT TO MAIN MENU")


        choice = input("Enter your choice: ")

        if choice == "1":
            print("GRADING SYSTEM")
            import activity2
            activity2.act2()
        elif choice == "2":
            print("STOP THE LOOP!")
            import activity3
            activity3.act3()
        elif choice == "3":
            print("CREATE A TRIANGLE")
            import activity4
            activity4.act4()
        elif choice == "4":
            print("AGE CATEGORIZED")
            import activity5
            activity5.act5()
        elif choice == "5":
            print("AGE CATEGORIZED v2")
            import activity6
            activity6.act6()
        elif choice == "6":
            print("GROCERY SYSTEM")
            import activity7
            activity7.act7()
        elif choice == "7":
            print("SUMMATION")
            import activity8
            activity8.act8()
        elif choice == "8":
            print("TRIANGLE")
            import activity9
            activity9.act9()
        elif choice == "9":
            print("DIAMOND v2")
            import activity10
            activity10.act10()
        elif choice == "10":
            print("DIAMOND")
            import activity11
            activity11.act11()
        elif choice == "11":
            print("ARROW UP")
            import activity12
            activity12.act12()
        elif choice == "12":
            print("DIAMOND NUMBERS 1 to 5")
            import activity13
            activity13.act13()
        elif choice == "13":
            print("The sum of all the numbers")
            import activity14
            activity14.act14()
        elif choice == "14":
            print("CREATE MORE TRIANGLE")
            import activity15
            activity15.act15()
        elif choice == "15":
            print("BANK SIMULATION PROGRAM")
            import activity16
            activity16.act16()
        elif choice == "16":
            print("ADDITIONAL ACTIVITY 1")
            import activity17
            activity17.act17()
        elif choice == "17":
            print("ADDITIONAL ACTIVITY 2")
            import activity18
            activity18.act18()
        elif choice == "18":
            print("ADDITIONAL ACTIVITY 3")
            import activity19
            activity19.act19()
        elif choice == "19":
            print("ADDITIONAL ACTIVITY 4")
            import activity20
            activity20.act20()
        elif choice == "20":
            print("ADDITIONAL ACTIVITY 5")
            import activity21
            activity21.act21()
        elif choice == "21":
            print("ADDITIONAL ACTIVITY 6")
            import activity22
            activity22.act22()
        elif choice == "22":
            print("ADDITIONAL ACTIVITY 7")
            import activity23
            activity23.act23()
        elif choice == "23":
            print("ADDITIONAL ACTIVITY 8")
            import activity24
            activity24.act24()
        elif choice == "24":
            print("ADDITIONAL ACTIVITY 9")
            import activity25
            activity25.act25()
        elif choice == "25":
            print("Returning to main menu...")
        else:
            print("Invalid choice. Please try again.")

# Run the program
main_menu()