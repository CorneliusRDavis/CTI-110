#Davis,Cornelius
#3/19/2025
#Using a for loop inside s while loop to print match



run_again = "yes"

while run_again != "no":
    user_num = int(input("enter an interger: "))
    if user_num < 0:
        print("Negative users arent allowed")
    else: #user_num < 0:
        for i in range(1,13):
            print(f"{user_num} * {i} = {user_num*i} ")
    run_again = input("would you like to run again? 'yes or no' ")
# While loop ends here
print("Program has concluded ............")


