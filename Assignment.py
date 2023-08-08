#Greet
import datetime
# get current time
current_time = datetime.datetime.now()
# extract hour from the current time
hour = current_time.hour
# greet user based on the time of the date
if 0 <= hour < 12:
    greeting = "Good morning!"
elif 12 <= hour < 18:
    greeting = "Good afternoon!"
else:
    greeting = "Good evening!"

print("\033[1mWECOME Visitor\033[0m")
print(greeting + "," + "nice to meet you")
print()

#Today
import datetime
def day_of_the_week():
    day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    today = datetime.datetime.now().weekday()
    return day_names[today]

def message_for_the_day():
    day = day_of_the_week()
    if day in ['Monday','Tuesday','Wednesday','Thursday','Friday']:
        print(f"Today is {day}, let go to work!")
    elif day == 'Saturday':
        print(f"Today is {day}, let go and party!")
    else:
        print(f"Happy {day}, let go to church!")
#main program
message_for_the_day()
print()
#Food App
print("\033[33m\033[1mWECOME TO FOOD MATAZ\033[0m\033[0m")
What_do_you_want_to_order = input("What do you want to order(Input what you want to order )?:")
# Vaidate food item
print("Order Confirmation,You ordered {}!".format(What_do_you_want_to_order))
print()
#Simpe Cacuator
print("\033[1m SIMPE CACUATOR \033[0m")
a = int(input("Input a number: "))
o = str(input("Input operator(e.g +,-,/ or *): "))
b = int(input("Input a number: "))

if o == "+":
    print("Answer = ",a+b)
if o == "-":
    print("Answer = ",a-b)
if o == "/":
    print("Answer = ",a/b)
if o == "*":
    print("Answer = ",a*b)
print()
#Nigeria Guessing Game
import datetime
def guess():
    print("\033[1mWECOME TO Nigeria GUESSING GAME!\033[0m")
    current_year = datetime.datetime.now().year
    Nigeria_age = current_year - 1960
    while True:
        guess = int(input("What is Nigeria's age?:"))
        if guess == Nigeria_age:
            print("Correct")
            break
        else:
            print("\033[91mWrong!.Try again\033[0m")
guess()
print()
#Prime number guessing game
def is_prime(number):
    if number < 2:
        return False
    for i in range(2,int(number**0.5)+1):
        if i % 1 == 0:
            return False
    return True
print()
#Guess the prime number game
def prime_guess():
    print("\033[1mWECOME TO PRIME NUMBER GUESSING GAME!\033[0m")
    while True:
        guess_prime = int(input("Guess a prime number between 1-70?:"))

        if guess_prime < 1 or guess_prime > 70:
            print("\033[91mNumber is not within the range 1-70!.Pease try again\033[0m")
        elif is_prime(guess_prime):
            print("Correct")
            break
        else:
            print("\033[91mWrong!.Try again\033[0m")
prime_guess()
print()
#Investment Cacuator
def investment_cacuator():
    print("\033[91m\033[1mIncrease rate is 10% per month\033[0m\033[0m")
    investment_amount = float(input("Enter amount you want to invest: "))
    monthy_interest_rate = 10/100 # 10% monthy interest
    num_of_months = int(input("Enter number of months: "))

    Tota_return = investment_amount * monthy_interest_rate * num_of_months
    Future_vaue = investment_amount + Tota_return
    print("Tota Return: #", round(Tota_return,))
    print("Future Vaue: #", round(Future_vaue,2))
investment_cacuator()

#oan Cacuator
def oan_cacuator():
    print("\033[91m\033[1mInterest rate is 10% per month\033[0m\033[0m")
    #Get oan amount from user
    oan_amount = float(input("Enter oan amount: #"))
    oan_amt = round(oan_amount,2)
    #Get number of months from user
    monthy_interest_rate = 10/100 # 10% monthy interest
    num_of_months = int(input("Enter number of months: "))
    #Cacuate interest per month
    monthy_interest = oan_amount * monthy_interest_rate
    monthy_intr = round(monthy_interest,2)
    #Tota repayment
    tota_repayment = oan_amount + (monthy_interest * num_of_months)
    tota_repay = round(tota_repayment,2)
    #dispay tota repayment
    print("       \033[1m\033[32moan Summary\033[0m\033[0m")
    print(f"oan Amount: #{oan_amt}")
    print(f"Number of month(s): {num_of_months}")
    print(f"Monthy Interet per Month: #{monthy_intr}")
    print(f"Tota Repayment: #{tota_repay}")
oan_cacuator()
print()
#Guess a number game
import random

def guessing_game():
    high_score = None
    pay_again = True

    while pay_again:
        target_number = random.randint(1,20)
        attempts = 0

        print("\033[34mWecome to the Guessing Game!\033[0m")
        print("\033[34mGuess a Number between 1 and 20.\033[1m\nNote:payer have ony seven trias \033[0m\033[0m")

        while attempts < 5:
            guess = int(input("Enter your guess:"))

            if guess < target_number:
                print("\033[31mToo ow!\033[0m")
            elif guess > target_number:
                print("\033[31mToo high!\033[0m")
            else:
                print("\033[32mCongratuations! You guess the correct number!\033[0m")
                if high_score is None or attempts < high_score:
                    high_score = attempts * 10
                    print(f"\033[32mNew high score: {high_score}\033[0m")
                break

            attempts += 1

        if attempts ==7:
            print(f"\033[1m\033[31mGame Over.\033[0m\033[0m\nThe correct number was {target_number}")
        pay_again = input("\033[32mDo you want to pay again? (yes/no):\033[0m ").ower() == "yes"

    print("\033[32mThank you for paying the Guessing Game!\033[0m")

guessing_game()