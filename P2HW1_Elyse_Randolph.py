#Elyse Randolph
#October 13 2024
#P2HW1
#Program takes a user's input budget and then subtracts various costs of a trip such as gas, lodging, and food.
print("This program calculates and displays travel expenses")
budget= int(input("Enter budget: ")) #takes users input for budget, destination name, gas, hotel, and food costs
destination= input("Enter your travel destination? ")
gas= int(input("How much do you think you will spend on gas? "))
hotel=int(input("Approzimately, how much will you need for accomodation/hotel? "))
food= int(input("Last, how much will you need for food? "))
print("")
print("---------Travel Expenses---------") #prints the values that the user entered into the program earlier
print("Location:".ljust(20),destination)
print("Initial Budget:".ljust(20),f'${budget:.2f}')
print("Fuel:".ljust(20),f'${gas:.2f}')
print("Accomodation:".ljust(20),f'${hotel:.2f}')
print("Food:".ljust(20),f'${food:.2f}')
print("---------------------------------")
print("")
input('Enter to exit')