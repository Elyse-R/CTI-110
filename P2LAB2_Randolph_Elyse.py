#Elyse Randolph
#October 6 2024
#P2LAB2
#Program creates a dictionary using preset values and prints information based on which entry the user selects
carModels = {
        'Camaro': 18.21,
        'Prius': 52.36,
        'Model S': 110,
        'Silverado': 26
    }
keys = carModels.keys()
print(keys)
userModel = input("Enter a vehicle to see its mpg: ")
print('The',userModel,f'gets {carModels[userModel]} mpg')
distance = float(input('How many miles will you drive the Prius? '))
print(f'{distance/carModels[userModel]:.2f}','gallon(s) of gas are needed to drive the',userModel,distance,"miles")
