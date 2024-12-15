#Elyse Randolph
#October 26 2024
#P3HW2
#Program takes input from user and then calculates the amount they are paid depending on how long they worked as well as overtime hours and pay
name = ''
numEmployee = 0
overtimeTotal = 0.0
regTotal = 0.0
grossTotal = 0.0

while name.lower() != "done":
    name = input("Enter employee's name or \"Done\" to terminate: ")
    if name.lower() == "done":
        break
    numEmployee += 1
    hoursWorked = float(input("How many hours did " + name + " work? "))
    payRate = float(input("What is " + name +"'s pay rate? "))       #User inputs the employee name, the hours worked, and the employee's pay rate


    if hoursWorked > 40:
        overtime = hoursWorked - 40
        overtimePay = overtime * payRate * 1.5
        overtimeTotal += overtimePay
    else:
        overtime = 0
        overtimePay = 0             #Checks if there was overtime worked and calculates the pay if there was any

    
    regPay = payRate * (hoursWorked - overtime)
    regTotal += regPay
    grossPay = overtimePay + regPay         #Create variables that calculate the total pay excluding overtime and the total including overtime 
    grossTotal += grossPay
    

    print("------------------------------")
    print("Employee name:   ",name)
    print("")
    print("Hours Worked   Pay Rate    OverTime    OverTime Pay    RegHour Pay     Gross Pay")
    print("-----------------------------------------------------------------------------------------")
    print(f'{hoursWorked:<15.1f}{payRate:<12.1f}{overtime:<12.1f}${overtimePay:<15.2f}${regPay:<16.2f}${grossPay:.2f}') #prints all of the information gathered above and formats it
    print('')
print('')
print("Total number of employees entered: ",numEmployee)
print("Total amount paid for overtime: $" + str(overtimeTotal))
print(f'Total amount paid for regular hours: ${regTotal:.2f}')
print("Total amount paid in gross: $" + str(grossTotal))
