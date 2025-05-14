#Davis,Cornelius
#05/02/2025
#P3LAB
#Using integer division and if/else statements
import random
def make_change(change):
    
    #Get float input from the user


    #Convert the float value into an integer
    change = int(change * 100)

    print(change)

        
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")
def main():
    amount_o = round(random.uniform(0.01, 100.0), 2)
    print(f"you owe ${amount_o:.2f}")
    
    cash_in = float(input("Enter amount into machine: "))
    change = cash_in - amount_o
    print(f"Your change is ${change:.2f}")
    make_change(change)

if __name__ == "__main__":
    main()