#Elyse Randolph
#November 10 2024
#P4HW1
#Program takes a list of grades for different test and outputs the lowest grade, highest grade, the sum of all of them, and the average


gradeList=[]
num = 1
gradeNum = int(input("How many scores do you want to enter? "))
sum = 0.0


while gradeNum > 0:
    grade = float(input("Enter score #" + str(num) +': ')) #Iterates through the loop the amount of times set in the gradeNum variable and adds the grades to a list
    if grade >= 0 and grade <= 100:
        gradeList.append(grade)
        num +=1
        gradeNum -=1
        sum += grade
    else:                                                  #Else activates if any number greater than 100 or less than 0 is input and repeats until valid input is detected
        print('')
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        while gradeNum > 0:
            grade = float(input("Enter score #" + str(num) +' again: '))
            if grade >= 0 and grade <= 100:
                gradeList.append(grade)
                num +=1
                gradeNum -=1
                sum += grade
                break
            else:
                print('')
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
            
lowGrade = min(gradeList)  #caclulates the lowest grade and takes it out of the list as well as calculates the average grade
gradeList.remove(lowGrade)
sum -= lowGrade
averageGrade = sum/len(gradeList)


if averageGrade >= 90:   #Checks the average grade and assigns a letter grade according to the criteria in the if statements
    letterGrade = 'A'
elif averageGrade >=80:
    letterGrade = 'B'
elif averageGrade >= 70:
    letterGrade = 'C'
elif averageGrade >= 60:
    letterGrade = 'D'
else:
    letterGrade = 'f'

print('')
print('--------Results--------')
print('Lowest Score  :',float(lowGrade)) #prints the lowest grade from the list above, the list of grades, the average grade, and letter grade
print('Modified List :', gradeList)
print('Scores average:', f'{averageGrade:.2f}') 
print('Grade         :',letterGrade)
print('--------------------------------')

