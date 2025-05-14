#Davis, Cornelius
#03/31/2025



employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter Hours Worked: "))
pay_rate = float(input("Enter Pay Rate: "))

print("-------------------")

regular_hours = ("")

overtime_rate_multiplier = 1.5

if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5) 
        regular_hours = 40
else:
    regular_hours = hours_worked


overtime_hours = max(0, hours_worked - 40)

overtime_pay = overtime_hours * (pay_rate * overtime_rate_multiplier)

regular_hours = hours_worked - overtime_hours

regular_pay = regular_hours * pay_rate

gross_pay = regular_pay + overtime_pay

print(f"Employee Name: {employee_name}")

print(f"Hours Worked: {hours_worked}")

print(f"Pay Rate: ${pay_rate:.2f}")

print(f"Overtime Hours: {overtime_hours}")

print(f"Overtime Pay: ${overtime_pay:.2f}")

print(f"Regular Pay: ${regular_pay:.2f}")

print(f"Gross Pay: ${gross_pay:.2f}")