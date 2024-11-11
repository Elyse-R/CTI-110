#Elyse Randolph
#November 10 2024
#P4HW1
#Program takes a list of grades for different test and outputs the lowest grade, highest grade, the sum of all of them, and the average


gradeList=[]
num = 1
gradeNum = int(input("How many scores do you want to enter? "))
sum = 0.0


while gradeNum > 0:
    grade = float(input("Enter score #" + str(num) +': '))
    if grade >= 0 and grade <= 100:
        gradeList.append(grade)
        num +=1
        gradeNum -=1
        sum += grade
    else:
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
            
lowGrade = min(gradeList)
gradeList.remove(lowGrade)
sum -= lowGrade
averageGrade = sum/len(gradeList)


if averageGrade >= 90:
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
print('Lowest Score  :',float(lowGrade)) #prints the lowest grade from the list above
print('Modified List :', gradeList)
print('Scores average:', f'{averageGrade:.2f}') #calculates the average of the grades in the totalGrades list
print('Grade         :',letterGrade)
print('--------------------------------')

