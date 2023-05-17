

# ### Day 1: Python Basics
# Start by installing Python and a text editor. Learn the basics of Python, such as: 
#  variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

# #### Exercise
# Simple Python Calculator Program: Write a simple program that does basic math operations including addition, subtraction, deletion, division, power, squareroot,etc,. 


#Simple Python Calculator Program: Write a simple program that does basic 
# math operations including addition, subtraction, deletion, division, power, 
# squareroot,etc,.

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #input choice of how to sort the calculation
    choice = input("Enter choice (1/2/3/4): ")
    #once u choose you input the number u want to calculate
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        #if you do not input a number a error will prevent you from proceeding

        if choice == '1':
            result = num1 + num2
            operator = '+'
        elif choice == '2':
            result = num1 - num2
            operator = '-'
        elif choice == '3':
            result = num1 * num2
            operator = '*'
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                operator = '/'
            else:
                print("Error: Cannot divide by zero.")
                continue

        print(num1, operator, num2, "=", result)
        #below after the calculation a prompt will ask you if you wish to proceed or not
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid input. Please enter a valid choice.")

print("Calculator program has ended.")
