#Elyse Randolph
#October 19 2024
#P3LAB
#Takes user input amount of money and breaks it down into the correct amount of bills and change

dollarAmount = float(input("Enter the amount of money as a float: "))
value = dollarAmount * 100

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
    dollarAmount %= 1
    if dime == 1:
        print(int(dime),"Dime")
    elif dime > 1:
        print(int(dime),"Dimes")


if value >= 5:
    nickel = dollarAmount // 5
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
