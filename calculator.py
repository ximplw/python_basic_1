# Simple calculator that performs basic arithmetic operations

first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = first_num + second_num
    print("Result:", result)
elif operation == '-':
    result = first_num - second_num
    print("Result:", result)
elif operation == '*':
    result = first_num * second_num
    print("Result:", result)
elif operation == '/':
    if second_num != 0:
        result = first_num / second_num
        print("Result:", result)
    else:
        result = "Error: Division by zero is not allowed."
        print(result)
else:
    result = "Error: Invalid operation"
    print(result)

