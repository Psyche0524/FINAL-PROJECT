#Create a program of filipino denomination using a function by Petalvero
import os

try:
    user = input("Input your name ---> ")
    initialDep = int(input("Input your initial deposit ---> "))

    def denomination(amount):           
        libo = amount // 1000
        tira = amount % 1000         #tira variable will update hanggang sa last filipino denomination
        
        limang_daan = tira // 500
        tira = tira % 500
        
        dalawang_daan = tira // 200
        tira = tira % 200
        
        isang_daan = tira // 100
        tira = tira % 100
        
        pipti = tira // 50
        tira = tira % 50
        
        bente = tira // 20
        tira = tira % 20
        
        sampu = tira // 10
        tira = tira % 10
        
        lima = tira // 5
        tira = tira % 5
        
        piso = tira // 1
        tira = tira % 1
        
        print(f"{libo} = 1000php \n{limang_daan} = 500php \n{dalawang_daan} = 200php \n{isang_daan} = 100php \n{pipti} = 50php \n{bente} = 20php \n{sampu} = 10php \n{lima} = 5php \n{piso} = 1php")
        print("\n\t\t\tTransaction Success...")
        
    while True:
        print("----------------------------------------------------------------------\n")
        print(f"Hi {user}, Welcome to CASH G Banking Program.\nCurrent Balance : {initialDep}php")
        ask = input("\nWould you like to : \n1.) Deposit \n2.) Withdraw \n3.) Denominate Balance \n4.) Exit \n\nSelect ---> ")
        os.system('cls')
        
        if ask == "1":
            amountDep = int(input("The amount to be deposit ---> "))
            initialDep += amountDep
            print("Deposit Exchange in PH Denomination...\n")
            denomination(amountDep)
            continue
        
        elif ask == "2":
            amountWithdraw = int(input("The amount to withdraw ---> "))
            if amountWithdraw > initialDep:
                print("Only withdraw with your remaining balance")
                break
            else:
                print("Withdraw Exchange in PH Denomination...\n")
                initialDep -= amountWithdraw
                denomination(amountWithdraw)
                continue
        
        elif ask == "3":
            print("Exchange in PH Denomination")
            denomination(initialDep)
            
        elif ask == "4":
            print("Program Terminated")
            break
        
        else:
            print("(Please only select from 1 to 4)")
            continue
except:
    print("The program only allowed papermoney and not centavos at the moment (please re-run the program).")