#Elyse Randolph
#October 13 2024
#P2HW2
#Program takes a list of grades for different test and outputs the lowest grade, highest grade, the sum of all of them, and the average
mod1 = float(input("Enter Module 1 grade: "))
mod2 = float(input("Enter Module 2 grade: "))
mod3 = float(input("Enter Module 3 grade: "))
mod4 = float(input("Enter Module 4 grade: "))
mod5 = float(input("Enter Module 5 grade: "))
mod6 = float(input("Enter Module 6 grade: ")) #sets up variables that store the user input grades

sumGrades = (mod1 + mod2 + mod3 + mod4 + mod5 + mod6)
totalGrades = [mod1,mod2,mod3,mod4,mod5,mod6] #Sets up variable to store the total of all grades added together and a list that stores all of the grades

print('')
print('--------Results--------')
print('Lowest Grade:'.ljust(20),min(totalGrades)) #prints the lowest grade from the list above
print('Highest Grade:'.ljust(20),max(totalGrades))#prints the highest grade from the list
print('Sum of Grades:'.ljust(20),sumGrades)       
print('Average:'.ljust(20), f'{sumGrades/len(totalGrades):.2f}') #calculates the average of the grades in the totalGrades list
print('--------------------------------')


