def activity1():
    print(f"Hello World")
def activity2():
    name = input("Please Enter Your Name : ")
    print(f"Hellows {name}")
def activity3():
    name = input("What is your name: ")
    age = input("How old are you: ")
    email = input("What is your email: ")
    birthday = input("When is your Birthday: ")
    address = input("Enter your Address: ")
    print(f"\nHi my name is {name} and I am {age} yrs old. I was born in {birthday} And I am from {address}. My email is {email}")
def activity4():
    print("========================================\n")
    num1 = eval(input("Number: "))
    num2 = eval(input("Number: "))
    op = input("Operators(+, -, /, x): ")

    if op == "+":
            print("Output:", num1 + num2)
    elif op == "-":
            print("Output:", num1 - num2)
    elif op == "/":
                print("Output:", num1 / num2)
    elif op == "x":
            print("Output:", num1 * num2)
    else:
            print("Invalid operator! \n\n")
    print("\n========================================")
def activity5():
    x = 5
    print(f"{x}")
    x = x + 10
    print(x)
    x = x + 15
    print(x)
    x = x + 20
    print(x)
    x = x + 25
    print(f"{x}\n")
def activity6():
    temp = int(input("Enter temperature in Fahrenheit: "))
    cel = (temp - 32) * 5 / 9
    cel_r = round(cel, 2)
    print(f"\nThe conversion of  {temp} degrees Fahrenhet is {cel_r} degrees celsius.\n")

def activity7():
    miner = input("Enter you name: ")
    mined = input("Did you mine gold today (yes/no) : ")
    gold = 0
    if mined.lower() == "yes":
        gold += 1
        print(f" Your total mined today is {gold} gold\n")
    elif mined.lower() == "no":
        print(f" You havent mined a gold today\n")
    else:
        print("Invalid error\n")
def activity8():
    passcode= input("Enter passkey >>> ") 
    if passcode.lower() == "hi":
        print("Hi")
        print("Love ya too, mwaa\n")
    else:
        print("wrong passkey!!")
        print("""Hint: HI yung password\n""")
def activity9():
    age = int(input("Enter your age: "))
    if age <= 1:
        print("You are a Toddler\n")
    elif age <= 8:
        print("You are a Pre-teen\n")
    elif age <= 14: 
        print("You are Teenager\n")
    elif age <= 19:
        print("You are in Early adulthood\n")
    elif age <= 32:
        print("You are in Mid adulthood\n")
    elif age <= 46:
        print("You are in Post adulthood\n")
    elif age >= 60:
        print("You are in your Senior\n")
    else:
        print("Invalid syntax\n")
def activity10():
    DLL = input("Are you a student of DLL? (yes/no??) : ")

    if DLL.lower() == "yes":
        print("Good Morning Student!","\nWelcome to the DLL Scholarship Form!")

        yearlv = input("What is your current year in DLL?")
        if yearlv.lower() == "freshman":
            print("Hello Freshmen of DLL!")
        elif yearlv.lower() == "sophomore":
            print("Hello Sophomore of DLL!") 
        elif yearlv.lower() == "junior":
            print("Konnichiwa Junior_kun of DLL!")
        elif yearlv.lower() == "senior":
            print("Welcome Senior of DLL!")
        else: 
                print("???")
        youNeed = input("Do you need this scholarship?? (y/n) : ")
        if youNeed.lower() == "yes":
            print ("Scholarship Granted :}")
        else:
            print("Okay thanks for using it")

def activity11():
    for repeat in range (1,11):
        print("Hello World")
def activity12():
    for y in range(10, 0, -1):
        print(y)
def activity13():
    num = int(input("Enter number: "))
    answer = 1
    for loop in range(num, 0, -1):
        print(loop)
        answer *= loop
    print(f"The factorial of {num} is: {answer}")
def activity14():
     for x in range(0,11):
        print(x, end=" ")
        for y in range(0, 11):
            print("*", end=" ")
        print()
def activity15():
    for x in range(0,11):
        print(x, end=" ")
        for y in range(0, x):
            print("*", end=" ")
        print()
def activity16():
    for x in range(1,11):
        for y in range(11, x, -1):
            print(" ",end=" ")
        for z in range(1, x+1):
            print("*", end=" ")
        for a in range(1, x+1):
            print("*", end=" ")
        print()
    #Second Triangle Shape Inverted
    for x in range(1,11):
        for y in range(1, x+1):
            print(" ",end=" ")
        for z in range(11, x,-1):
            print("*", end=" ")
        for a in range(11, x,-1):
            print("*", end=" ")
        print()

def activity17():
    gela = int(input("Enter a number: "))
    for x in range(1,11):
        for y in range(1, gela + 1):
            print(f"{x} x {y} = {x*y}", end="\t")
        print()
def activity18():
    gela = int(input("Enter a number: "))
    for a in range(1,5):
        for x in range(1,gela +1 ):
            for y in range(1, a + 1):
                print("*", end= " ")

            for z in range(5, a, -1):
                print(" ", end=" ")
        print()
def activity19():
    while True:
        name = input("Are You Happy? (yes/ no): ")
        if name.lower() == "yes":
            print("I See Good For you!")
            break
        elif name.lower() == "no":
            print("Okay Comeback when your happy\n")
            break
        else:
            print("Invalid input exiting")
            break
def activity20():
    condition = True
    num = 0
    while condition == True:
        question = str(input("Do you want to add triangles (yes/no): "))
        if question.lower() == "no":
            print("PROGRAM TERMINATED\n")
            break
        else:
            num += 1
            for a in range(1,5):
                for x in range(1, num+1 ):
                    for y in range(1, a + 1):
                            print("*", end= " ")
                            
                    for z in range(5, a, -1):
                            print(" ", end=" ")
                print()
        continue
def activity21():
    print("\n\t========================== ACTIVITY 21 ==========================\n")
    tuloy = True
    nameno = 0
    while tuloy == True:
        name = input("Enter a name: ")
        

        if name.lower()=="stop":
            print("Okay tama na\n")
            print(f"You have entered a total of {nameno} names!")
            break

        else:
            print("type 'stop' if you want to terminate the program\n")
            nameno += 1
            continue
def activity22():
    def activity22():
        def activity1():
            print("Hello World")
        activity1()
    activity22()
def activity23():
    def factorial(number):
        fact = 1
        for x in range(number, 0, -1):
            fact *= x

        return fact

    print(f"the factorial of 13 is {factorial(13)}")
def activity24():
       pass
def activity25():
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)
def code_challenge1():
    print("\t\t\t\t\t\t\t\t\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t*")
def code_challenge2():
    name = input("Please enter your name:")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b*\t"+("  Hello! " +name)+"\t\t*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*")
def code_challenge3():
    print("===============================================================BIO DATA===============================================================")
    Name = input("\n\tName: ").strip() .title()
    Mobile = input("\tMobile No. ")
    Email = input("\tEmail: ")
    Educ = input("\tEducation: ")
    Address = input("\tAddress: ")
    birth = input("\tDate of Birth: ")
    gen = input("\tGender: ")
    marital_Status = input("\tMarital Status: ")
    Religion = input("\tReligion: ")
    print("============================================================Family Details============================================================")
    Fname = input("\tFathers Name: ").strip() .title()
    F_accupation = input("\tFathers Accupation: ")
    Mname = input("\tMothers Name: ").strip() .title()
    M_accupation = input("\tMothers Accupation: ")
    print("==============================================================================================================================")
    print("INFORMATION: "+"\nName: " + Name + "\nMobile Number: " + Mobile + "\nEmail: " + Email + "\nEducation: " + Educ + "\nAddress: " + Address + "\nBirth Date: " + birth + "\nGender: " + gen +  "\nMarital Status: " + marital_Status + "\nReligion: " + Religion + "\n\nFathers Name: " + Fname + "\nFathers Accupation: " + F_accupation + "\nMothers Name: " + Mname +"\nMothers Accupation: "+ M_accupation +"\n\nThank you for answering!")
    print("==============================================================================================================================")
    print()
def code_challenge4():
    no1 = eval(input("type first number >>"))
    no2 = eval(input("type second number >>"))
    answer1 = no1 + no2

    answer2 = no1 - no2

    answer3 = no1 *(no2) 

    answer4  = no1 / no2

    answer5  = no1 ** no2 

    answer6  = no1 % no2 

    answer7  = no1 // no2 

    print("the sum of",no1," and ",no2,"is",answer1,":)")
    print("the difference of",no1,"and",no2,"is",answer2)
    print("the product of",no1,"and",no2,"is",answer3)
    print("the quotient of",no1,"and",no2,"is",answer4)
    print("the exponent of",no1,"and",no2,"is",answer5)
    print("the remainder of",no1,"and",no2,"is",answer6)
    print("the floor division of",no1,"and",no2,"is",answer7)
def code_challenge5():
        prelim = eval(input("Prelim Score: "))
        midterm = eval(input("Midterm Score: "))
        semi_finals = eval(input("Semi Final Score: "))
        finals = eval(input("Finals Score: "))
        quiz = eval(input("Quiz Score: "))
        project = eval(input("Project Score: "))

        Grade = (prelim * 0.15) + (midterm * 0.15) + (semi_finals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

        if Grade > 100:
            print("Grade is Over 100!")
        elif Grade >= 75:
            print("You PASSED!!")
        elif Grade < 75:
            print("Good Luck Next Life :( ")
        else:
            print("Huh?")
def code_challenge6():
    prelim = eval(input("Prelim Score: "))
    midterm = eval(input("Midterm Score: "))
    semi_finals = eval(input("Semi Final Score: "))
    finals = eval(input("Finals Score: "))
    quiz = eval(input("Quiz Score: "))
    project = eval(input("Project Score: "))

    Grade = (prelim * 0.15) + (midterm * 0.15) + (semi_finals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

    if Grade > 100:
        print("Grade is Over 100!")
    elif Grade >= 75:
        print("You PASSED!!")
    elif Grade < 75:
        print("Good Luck Next Life :( ")
    else:
        print("Huh?")
def code_challenge7():
    isBuy = input("Do you want to make a grocery purchase (yes/no): ")

    if isBuy.lower() == "yes" :
        item_name = input("Enter the item name: ")
        item_price = eval(input("Enter the price of the item: "))
        age = eval(input("Enter your age: "))
        cash = eval(input("Enter the amount of cash you have given: "))

        discount_amount = round(item_price * 0.060, 4)
        discount_price = round(item_price - discount_amount, 4)
        tax_amount = round(item_price * 0.155, 4)
        tax_price = round(item_price + tax_amount)

    if age >= 60:
        print(f"\nHi, our dear customer, you purchased a/an {item_name}, that costs {item_price}Php plus a 5.2% discount {discount_amount}Php to your total purchase. ")
        print(f"Total: {round(item_price - discount_amount, 4)} ")
        print(f"Change: {round(cash - discount_price, 4)} ")
        print("Thank you for shopping, see you next time! ")

    elif age >=18:
        print(f"\nHello!, you have purchased {item_name}, that costs {item_price}Php plus a 14.3% tac {tax_amount}Php to your total purchase. ")
        print(f"Total: {round(item_price + tax_amount, 4)} ")
        print(f"Change: {round(cash - tax_price, 4)} ")
        print("Thank you for shopping,Hope to see you next time! ")
def code_challenge8():
        odd = 0
        even = 0
        sum = 0
        for x in range(1, 11):
            num = eval(input(f"Enter #{x} :"))
            sum += num
            if num % 2 == 0:
                even += num
            else:
                odd += num

        print(f"the sum of all the numbers given is {sum}")
        print(f"the sum of all the numbers given is {odd}")
        print(f"the sum of all the numbers given is {even}")
def code_challenge9():
        for x in range(1, 6):
            for y in range(1, x + 1):
                print("*",end=" ")
            print()
def code_challenge10():
    #arrow up
    for x in range(1, 6):
        for y in range(6, x , -1):
            print(" ",end=" ")
        for z in range(1, x +1 ):
            print("*",end=" ")		
        for a in range(1, x +1 ):
            print("*",end=" ")
        print()
    #arrow down
    for x in range(1, 6):
        for y in range(1, x + 1):
            print(" ",end=" ")
        for z in range(6, x, -1):
            print("*",end=" ")
        for a in range(6, x, -1):
            print("*",end=" ")
        print()
def code_challenge11():
    #arrow up
    for x in range(1,5):
        for y in range(5,x,-1):
            print("",end="")
        for z in range(1,x):
            print("*",end="")
        for a in range(0,x):
            print("*",end="")
        print()

    #arrow down
    for x in range(1,6):
        for y in range(1,x):
            print("",end="")
        for z in range(6,x,-1):
            print("*",end="")
        for a in range(5,x,-1):
            print("*",end="")
        print()
def code_challenge12():
    for x in range (1, 5):
        for y in range(5, x, -1):
            print(" ", end=" ")
        for z in range (1, x):
            print("*", end=" ")
        for a in range (0, x):
            print("*", end=" ")
        print()

    for i in range (x):
        for j in range (x-1):
            print(" ", end=" ")
        print("* * *")
def code_challenge13():
        for x in range (1, 7):
            for y in range (6, x, -1):
                print(" ", end=" ")
            for z in range (x, 1, -1):
                print(z, end=" ")
            for a in range (1, x + 1):
                print(a, end=" ")
            print()

        for x in range (5, 0, -1):
            for y in range (6, x, -1):
                print(" ", end=" ")
            for z in range (x, 1, -1):
                print(z, end=" ")
            for a in range (1, x + 1):
                print(a, end=" ")
            print()
def code_challenge14():
    cont = True
    x = 0

    while cont == True: 
        num = eval(input("Enter a number: "))
        if num == 0:
            print("Program Terminated")
            print(f"The total of the numbers you enter is {x}.")
            break
        else:
            x += num 
            continue
def code_challenge15():
    import os

    isTuloy = True
    no = 0


    for x in range (1, 6):
        for repeat in range (1 , no + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
                for z in range (6, x, -1):
                    print(" ",end=" ")
                print()
                
    while isTuloy == True:
        ask = input("Would you like to add a triangle [y/n?] -----> ")

        if ask.lower() == "no":
            print()
            print("::::PROGRAM TERMINATED::::")
            print()
            break
            isTuloy = False
        if ask.lower() == "n":
            print("==========================")
            print("::::PROGRAM TERMINATED::::")
            print("==========================")
            break
            isTuloy = False
        if ask.lower() == "yes":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for repeat in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        if ask.lower() == "y":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for repeat in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("Invalid Selection! Try again...")
            continue

def code_challenge16():
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

    accounts = {}

    def create_account(name, initial_deposit):
        if name in accounts:
            print(f"Account with name '{name}' already exists.")
        else:
            accounts[name] = initial_deposit
            print(f"Account created for '{name}' with an initial deposit of PHP {initial_deposit}.")

    def check_balance(name):
        if name in accounts:
            print(f"Current balance for '{name}': PHP {accounts[name]}")
        else:
            print("Account does not exist.")

    def denomination_breakdown(amount):
        print("Denomination breakdown:")
        for denom in denominations:
            count = amount // denom
            if count > 0:
                print(f"{denom} x {count}")
            amount %= denom

    def deposit(name, amount):
        if name in accounts:
            accounts[name] += amount
            print(f"Deposited PHP {amount} to '{name}'. New balance: PHP {accounts[name]}")
            denomination_breakdown(amount)
        else:
            print("Account does not exist.")

    def withdraw(name, amount):
        if name in accounts:
            if accounts[name] >= amount:
                accounts[name] -= amount
                print(f"Withdrew PHP {amount} from '{name}'. New balance: PHP {accounts[name]}")
            else:
                print("Insufficient balance!")
        else:
            print("Account does not exist.")

    def main():
        while True:
            print("\n--- BANK SIMULATION PROGRAM ---")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit Program")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter account name: ")
                initial_deposit = eval(input("Enter initial deposit: "))
                create_account(name, initial_deposit)
            elif choice == "2":
                name = input("Enter account name: ")
                amount = eval(input("Enter amount to deposit: "))
                deposit(name, amount)
            elif choice == "3":
                name = input("Enter account name: ")
                amount = eval(input("Enter amount to withdraw: "))
                withdraw(name, amount)
            elif choice == "4":
                name = input("Enter account name: ")
                check_balance(name)
            elif choice == "5":
                print("Thank you for using the Bank Simulation Program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    tuloy = True
    while tuloy == True:
        print("\n\t\t\t\t\t============================================================\n")
        print("\t\t\t\t\t\t\tWelcome to my program! ")
        print("\n\t\t\t\t\t============================================================\n")
        print("\n\t\t\t\t\t=======================| Activities |=======================\n")
        print("\t\t\t\t\t|| Act1 - activity_1                      Act14 - activity_14 ||")
        print("\t\t\t\t\t|| Act2 - activity_2                      Act15 - activity_15 ||")
        print("\t\t\t\t\t|| Act3 - activity_3                      Act16 - activity_16 ||")
        print("\t\t\t\t\t|| Act4 - activity_4                      Act17 - activity_17 ||")
        print("\t\t\t\t\t|| Act5 - activity_5                      Act18 - activity_18 ||")
        print("\t\t\t\t\t|| Act6 - activity_6  13 -   activity 13  Act19 - activity_19 ||")
        print("\t\t\t\t\t|| Act7 - activity_7                      Act20 - activity_20 ||")
        print("\t\t\t\t\t|| Act8 - activity_8                      Act21 - activity_21 ||")
        print("\t\t\t\t\t|| Act9 - activity_9                      Act22 - activity_22 ||")
        print("\t\t\t\t\t|| Act10 - activity_10                    Act23 - activity_23 ||")
        print("\t\t\t\t\t|| Act11 - activity_11                    Act24 - activity_24 ||")
        print("\t\t\t\t\t|| Act12 - activity_12                    Act25 - activity_25 ||")
        print("\n\t\t\t\t\t==========================================================\n\n")


        print("\n\t\t\t\t\t=======================| Code Challenges |=========================\n")
        print("\t\t\t\t\t|| Code_1 - Code_Challenge 1             Code_9 - Code_Challenge 9   ||")
        print("\t\t\t\t\t|| Code_2 - Code_Challenge 2             Code_10 - Code_Challenge 10 ||")
        print("\t\t\t\t\t|| Code_3 - Code_Challenge 3             Code_11 - Code_Challenge 11 ||")
        print("\t\t\t\t\t|| Code_4 - Code_Challenge 4             Code_12 - Code_Challenge 12 ||")
        print("\t\t\t\t\t|| Code_5 - Code_Challenge 5             Code_13 - Code_Challenge 13 ||")
        print("\t\t\t\t\t|| Code_6 - Code_Challenge 6             Code_14 - Code_Challenge 14 ||")
        print("\t\t\t\t\t|| Code_7 - Code_Challenge 7             Code_15 - Code_Challenge 15 ||")
        print("\t\t\t\t\t|| Code_8 - Code_Challenge 8             Code_16 - Code_Challenge 16 ||")
        print("\n\n\t\t\t\t\t\t\t\t\t\t\t0 - Exit")
        print("\n\t\t\t\t\t=================================================================\n\n")

        gela = input ("Enter a number:")
        if gela == "Exit" or gela == "0":
            break
        elif gela != "Exit":
            if gela == "Act1":
                activity1 ()
                continue
            elif gela == "Act2":
                activity2()
                continue
            elif gela == "Act3":
                activity3()
                continue
            elif gela == "Act4":
                activity4()
                continue
            elif gela == "Act5":
                activity5()
                continue
            elif gela == "Act6":
                activity6()
                continue
            elif gela == "Act7":
                activity7()
                continue
            elif gela == "Act8":
                activity8()
                continue
            elif gela == "Act9":
                activity9()
                continue
            elif gela == "Act10":
                activity10()
                continue
            elif gela == "Act11":
                activity11()
                continue
            elif gela == "Act12":
                activity12()
                continue
            elif gela == "Act13":
                activity13()
                continue
            elif gela == "Act14":
                activity14()
                continue
            elif gela == "A15":
                activity15()
                continue
            elif gela == "Act16":
                activity6()
                continue
            elif gela == "Act17":
                activity17()
                continue
            elif gela == "Act18":
                activity18()
                continue
            elif gela == "Act19":
                activity19()
                continue
            elif gela == "Act20":
                activity20()
                continue
            elif gela == "Act21":
                activity21()
                continue
            elif gela == "Act22":
                activity22()
                continue
            elif gela == "Act23":
                activity23()
                continue
            elif gela == "Act24":
                activity24()
                continue
            elif gela == "Act25":
                activity25()
                continue
            elif gela == "Code_1":
                code_challenge1()
                continue
            elif gela == "Code_2":
                code_challenge2()
                continue
            elif gela == "Code_3":
                code_challenge3()
                continue
            elif gela == "Code_4":
                code_challenge4()
                continue
            elif gela == "Code_5":
                code_challenge5()
                continue
            elif gela == "Code_6":
                code_challenge6()
                continue
            elif gela == "Code_7":
                code_challenge7()
                continue
            elif gela == "Code_8":
                code_challenge8()
                continue
            elif gela == "Code_9":
                code_challenge9()
                continue
            elif gela == "Code_10":
                code_challenge10()
                continue
            elif gela == "Code_11":
                code_challenge11()
                continue
            elif gela == "Code_12":
                code_challenge12()
                continue
            elif gela == "Code_13":
                code_challenge13()
                continue
            elif gela == "Code_14":
                code_challenge14()
                continue
            elif gela == "Code_15":
                code_challenge15()
                continue
            elif gela == "Code_16":
                code_challenge16()
                continue

    main()