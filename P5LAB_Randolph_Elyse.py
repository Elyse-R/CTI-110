#Elyse Randolph
#November 18 2024
#P5LAB
#Generates a random price and calculates the amount of change returned to the user when they input a certain payment to be given
import random

def disperse_change(dollarAmount):
    value = int(round(dollarAmount * 100))          

    if value >= 100:
        dollar = value // 100
        value %= 100
        if dollar == 1:
            print(int(dollar),"Dollar")
        elif dollar > 1:
            print(int(dollar),"Dollars")


    if value >= 25:
        quarter =  value // 25
        value %= 25
        if quarter == 1:
            print(int(quarter),"Quarter")
        elif quarter > 1:
            print(int(quarter),"Quarters")


    if value >= 10:
        dime = value // 10
        value %= 10
        if dime == 1:
            print(int(dime),"Dime")
        elif dime > 1:
            print(int(dime),"Dimes")


    if value >= 5:
        nickel = value // 5
        value %= 5
        if nickel == 1:
            print(int(nickel),"Nickel")
        elif nickel > 1:
            print(int(nickel),"Nickels")


    if value >= 1:
        penny = value // 1
        if penny == 1:
            print(int(penny),"Penny")
        elif penny > 1:
            print(int(penny),"Pennies")

paymentAmount = round(random.uniform(0.01, 100.00), 2)

print("You owe $" + str(paymentAmount))
customerCash = float(input("How much cash will you put in the self-checkout? "))
if customerCash > 0:
    change = customerCash - paymentAmount
    change = round(change, 2)

    print(f'Change is: ${change:.2f}')
    print("")

    disperse_change(change)
else:
    print("Please enter a valid amount")
    print("")
    print("You owe $" + str(paymentAmount))
    
    customerCash = float(input("How much cash will you put in the self-checkout? "))
    change = customerCash - paymentAmount
    change = round(change, 2)

    print(f'Change is: ${change:.2f}')
    print("")

    disperse_change(change)
