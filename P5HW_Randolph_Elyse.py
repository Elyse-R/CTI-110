#Elyse Randolph
#November 24 2024
#P5HW
#User can select from being given a question that adds two random numbers or subtracts to random numbers. The user is also given the option to end the program
import random


def addingNum():    
    sumAnswer = 0
    sumNum = 1
    randomSum1 = random.randint(1,999)
    randomSum2 = random.randint(1,999)
    print(' '+ str(randomSum1))
    print('+' + str(randomSum2))
    print('')
    sumNum = randomSum1 + randomSum2
    print('Enter answer.')
    sumAnswer = int(input(''))
    guesses = 1
    while sumAnswer != sumNum:        
        if sumAnswer > sumNum:
            print('Sorry, guess is too high.')
            print('')
            sumAnswer = int(input('Try again: '))
            guesses += 1
        elif sumAnswer < sumNum:
            print('Sorry, guess is too low.')
            print('')
            sumAnswer = int(input('Try again: '))
            guesses += 1
    if sumAnswer == sumNum:
            print('Congratulations!!!! Your answer is correct.')
            print('Number of guesses: ' + str(guesses))
            print('')
def subtractNum():
    subAnswer = 0
    subNum = 1
    randomSub1 = random.randint(1,999)
    randomSub2 = random.randint(1,999)
    print(' '+ str(randomSub1))
    print('-' + str(randomSub2))
    print('')
    subNum = randomSub1 - randomSub2
    print('Enter answer.')
    subAnswer = int(input(''))
    guesses = 1
    while subAnswer != subNum:        
        if subAnswer > subNum:
            print('Sorry, guess is too high.')
            print('')
            subAnswer = int(input('Try again: '))
            guesses += 1
        elif subAnswer < subNum:
            print('Sorry, guess is too low.')
            print('')
            subAnswer = int(input('Try again: '))
            guesses += 1
    if subAnswer == subNum:
            print('Congratulations!!!! Your answer is correct.')
            print('Number of guesses: ' + str(guesses))
            print('')


menuOption = 0
while menuOption != 3:
    print('Welcome to Math Quiz')
    print('')
    print('')
    print('MAIN MENU')
    print('------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('')
    menuOption = 0
    menuOption = int(input('Please choose one of the menu options: '))
    if menuOption == 1:
        addingNum()
    elif menuOption == 2:
        subtractNum()
    elif menuOption == 3:
        print('Thank you for plaing...')
        print('Bye!!')
    else:
        print('Please enter a valid option.')
        print('')
    
