#Elyse Randolph
#September 27 2024
#P1HW2
#Program takes a user's input budget and then subtracts various costs of a trip such as gas, lodging, and food.
print("This program calculates and displays travel expenses")
budget= int(input("Enter budget: ")) #takes users input for budget, destination name, gas, hotel, and food costs
destination= input("Enter your travel destination? ")
gas= int(input("How much do you think you will spend on gas? "))
hotel=int(input("Approzimately, how much will you need for accomodation/hotel? "))
food= int(input("Last, how much will you need for food? "))
print("")
print("-----Travel Expenses-----") #prints the values that the user entered into the program earlier
print("Location:",destination)
print("Initial Budget:",budget)
print("")
print("Fuel:",gas)
print("Accomodation:",hotel)
print("Food:",food)
print("Remaining Balance:",budget-(gas+hotel+food)) #Adds the total costs of the trip and subtracts them from the budget to show remaining funds
