import datetime
#Greet
#get current time
current_time = datetime.datetime.now()
#extract hour
hour = current_time.hour
#greet based on time of the day
if hour >=0 and hour < 12:
    greeting="Good morning!"
elif hour >=12 and hour < 18:
    greeting="Good afternoon!"
else:
    greeting="Good evening!"
print("\033[1mWelcome Visitor\033[0m")
print(f"{greeting} David, nice to meet you.")

#Today
def day_of_the_week():
    day_name=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    today=datetime.datetime.now().weekday()
    return day_name[today]
def message_of_the_day():
    day = day_of_the_week()
    if day in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
        print(f"Today is {day}, let go to work!")
    elif day == 'Saturday':
        print(f"Today is {day}, let go and party!")
    else:
        print(f"Happy {day}, let go to church!")
#run the program
message_of_the_day()
print()

#Food
print("\033[1mFood\033[0m")
order = input("What do you want to order?(input the food you want to order):")
#validate food order
print(f"Order confirmation!, you ordered {order}")
print()
#Simple Calculator
print("\033[1mSimple Calculator\033[0m")
num1 = int(input("first number: "))
op = input("Input operator(e.g +,-,/ or *): ")
num2 = int(input("input second number: "))
if op == "+":
    print("Answer = ",num1+num2)
elif op == "-":
    print("Answer = ",num1-num2)
elif op == "/":
    print("Answer = ",num1/num2)
elif op == "*":
    print("Answer = ",num1*num2)
else:
    print("math error")
print()

#Nigeria age
print("\033[1mGuess Nigeria's age\033[0m")
print("Player only have three(3) trails")
def nigeria_age():
        current_year = datetime.datetime.now().year
        nigeria_age = current_year - 1960
        attempts = 0
        while attempts < 3:
            age = int(input("Guess nigeria age:"))
            if age == nigeria_age:
                print("Correct")
                break
            else:
                print("Wrong! try again")
            attempts +=1
        if attempts == 3:
            print(f"Game Over! nigeria's age is {nigeria_age}")
        print("Thank you for playing the guessing game")
nigeria_age()
print()

#Investment calculator
print("\033[1mInvestment calculator\033[0m")
def investment_calculator():
    print("Increase is 10% per month")
    investment_amount = int(input("How much do you want to invest?: #"))
    monthly_increase_rate = 10/100 #10% monthly interest
    num_of_months = int(input("Enter number of month(s): "))
    Total_return = investment_amount * monthly_increase_rate * num_of_months
    Future_value = investment_amount + Total_return
    print("Investment Summary")
    print(f"Invested Amount: #{investment_amount}")
    print(f"Duration: {num_of_months} month(s)")
    print("Total Return: #",round((Total_return),2))
    print("Future Value: #",round((Future_value),2))
investment_calculator()
print()

#Loan calculator
print("\033[1mLoan calculator\033[0m")
def loan_calculator():
    print("Interest rate is 10% per month")
    Loan_amount = int(input("Enter Loan Amount: #"))
    monthly_intrest_rate = 10 / 100  # 10% monthly interest
    num_of_months = int(input("Enter number of month(s): "))
    #Calcuate interest per month
    monthly_intrest = Loan_amount * monthly_intrest_rate
    monthly_intrest = round(monthly_intrest,2)
    intrest = monthly_intrest * num_of_months
    Total_repayment = Loan_amount + intrest
    Total_repayment = round(Total_repayment,2)
    print("Loan Summary")
    print(f"Loan Amount: #{Loan_amount}")
    print(f"Duration: {num_of_months} month(s)")
    print("Monthly Intrest: #", round((monthly_intrest), 2))
    print("Total Repayment: #", round((Total_repayment), 2))
loan_calculator()
print()

#guess number
print("\033[1mGuess a number between 1 and 20\033[0m")
print("Player only have five(5) trails")
import random
def guess_number():
    play_again = True
    while play_again:
        target = random.randint(1,20)
        attempts = 0
        while attempts < 5:
            number = int(input("Enter Your Guess: "))
            if number > target:
                print("Too high!")
            elif number < target:
                print("Too low!")
            else:
                print("Congratulation! you guessed right")
                break
            attempts +=1
        if attempts ==5:
            print(f"Game Over! The number is {target}")
        play_again = input("\033[32mDo you want to play again? (y/n):\033[0m ").lower() == "y"
    print("Thank you for playing the guessing game")
guess_number()
