print("CALCULATOR BY DHRUV GUPTA, ROLL NUMBER:2024UC18045")
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide (x, y):
    if y != 0:
        return x/y
    else:
        return "Error! Division by zero." # Input from user

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
continue_calculating = True
while continue_calculating == True:
    print('''Choose an operation:
            1.Add
            2.Subtract
            3.Multiply
            4.Divide
            ''')
# Taking choice from user
    choice = input("Enter your choice (1/2/3/4): ") # Performing operations based on user choice
    if choice == "1":
        print("Result:", add (num1, num2))
    elif choice == "2":
        print("Result:", subtract (num1, num2))
    elif choice == "3":
        print("Result: ", multiply (num1, num2))
    elif choice == "4":
        print("Result:", divide (num1, num2))
    else:
        print("Invalid input! Please select a valid operation.")

    continue_choice = input("Do you want to perform another calculation? (y/n): ")
    if continue_choice.lower()=='y':
        continue_calculating = True
    elif continue_choice.lower() == 'n':
        continue_calculating = False
    else:
        print("Invalid input! Exiting the calculator.")

