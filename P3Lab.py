# Davis, Cornelius
# March/03/03
# P3LAB
# Use if/else statements to determine coin combination

# Get a float from user and convert to interger
input_money = float(input( "Enter the amount of money as float :$"))

money = int(input_money * 100)

#print (money)

# Calculate number of whole dollars 
num_dollars = money // 100
print(f"Num dollars: {num_dollars}")

# Remove the dollars from the amount of money
money = money - (num_dollars * 100)

#print(f"the remaining money is: {money}")


# Calculate number of quarters 
num_quarters = money // 25
#print(f"Num Quarters: {num_quarters}")

# Remove the quarters from the amount of money
money = money - (num_quarters * 25)

#print(f"the remaining money is: {money}")


# Calculate number of dimes 
num_dimes = money // 10
#print(f"Num Dimes: {num_dimes}")

# Remove the dimes from the amount of money
money = money - (num_dimes * 10)

#print(f"the remaining money is: {money}")


# Calculate number of nickles 
num_nickles = money // 5
#print(f"Num nickles: {num_nickles}")

# Remove the nickles from the amount of money
money = money - (num_nickles * 5)

#print(f"the remaining money is: {money}")

num_pennies = money 

# Dispaly coins/dollars neeeded only if they are used 
# Ensure all grammar is correct 
print()
print()
print()

print(f"{input_money:.2f}")

# Display Dollar

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
else:
    print(f"{num_dollars} Dollar")

# Display Quarter

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
else:
    print(f"{num_quarters} Quarter")

# Display Dime

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
else:
    print(f"{num_dimes} Dime")

# Display Nickles

if num_nickles > 0:
    if num_nickles == 1:
        print(f"{num_nickles} Nickle")
else:
    print(f"{num_nickles} Nickle")

# Display Pennies

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Pennie")
else:
    print(f"{num_pennies} Pennie")

# If no change is due display no change 
 
if input_money <= 0.00:
    print("no change")