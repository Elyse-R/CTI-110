#Elyse Randolph
#October 26 2024
#P3HW2
#Program takes input from user and then calculates the amount they are paid depending on how long they worked as well as overtime hours and pay

name = input("Enter employee's name: ")
hoursWorked = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))       #User inputs the employee name, the hours worked, and the employee's pay rate


if hoursWorked > 40:
    overtime = hoursWorked - 40
    overtimePay = overtime * payRate * 1.5
else:
    overtime = 0
    overtimePay = 0             #Checks if there was overtime worked and calculates the pay if there was any

    
regPay = payRate * (hoursWorked - overtime)
grossPay = overtimePay + regPay         #Create variables that calculate the total pay excluding overtime and the total including overtime 



print("------------------------------")
print("Employee name:   ",name)
print("")
print("Hours Worked   Pay Rate    OverTime    OverTime Pay    RegHour Pay     Gross Pay")
print("-----------------------------------------------------------------------------------------")
print(f'{hoursWorked:<15.1f}{payRate:<12.1f}{overtime:<12.1f}${overtimePay:<15.2f}${regPay:<16.2f}${grossPay:.2f}') #prints all of the information gathered above and formats it
