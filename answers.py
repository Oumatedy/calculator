# Getting user input for two numbers and an operation
# Performing the operation and displaying the result
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Performing the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")  # f-string
elif operation == '-':
    result = num1 - num2 
    print(f"{num1} - {num2} = {result}") # f-string
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}") # f-string
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}") # f-string
    else:
        print("Error: Division by zero is not allowed.") 
else:
    print("Invalid operation. Please enter +, -, *, or /.") 
