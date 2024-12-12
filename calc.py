# functions 
def print_menu():
    print("=========================")
    print("1) sum")
    print("2) subtract")
    print("3) multiply")
    print("4) division")

print_menu()
option = input("Select the option")

num1 = float(input("Please provide a number"))
num2 = float(input("Please provide a second number"))

# proceed with the logic to calculate the total

if option == "1":
    total = num1 + num2
    print(" the total is: " + str(total))
elif option == "2":
    total = num1 - num2
    print(" the total is: " + str(total))
elif option == "3":
    total = num1 * num2
    print(" the total is: " + str(total))
elif option == "4":
    if num2 == 0:
        print("youre trying to divide by zero")
    else:
        total = num1 / num2
        print(" the total is: " + str(total))

