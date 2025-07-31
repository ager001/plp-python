# simplest calculator program that performs simple mathematics operations

# Here I am asking the user to randomly enter two numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Here I am asking the user to enter the operation they want to perform
operation = input("Enter an operation (+, -, *, /): ")

# Here I am performing the operation based on user input
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")