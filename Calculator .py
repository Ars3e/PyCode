import math

# Function to get numbers from the user with advanced exception handling
def get_numbers(single=False):
    while True:
        try:
            if single:
                return float(input("Enter the number: ")),
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Basic mathematical operations
def add(num1, num2): return num1 + num2
def subtract(num1, num2): return num1 - num2
def multiply(num1, num2): return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        return None
    return num1 / num2
def sqrt(num):
    if num < 0:
        print("Error: Cannot calculate the square root of a negative number.")
        return None
    return math.sqrt(num)

# Function to perform an operation before the square root
def operation_before_sqrt(num1, num2, operation):
    ops = {
        'a': add(num1, num2),
        'b': subtract(num1, num2),
        'c': multiply(num1, num2),
        'd': divide(num1, num2)
    }
    result = ops.get(operation)
    if result is None:
        return None
    return sqrt(result)

# Main function for the calculator
def calculator():
    print("Welcome to the Calculator!")

    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide,
        '5': sqrt,
        '6': operation_before_sqrt
    }

    while True:
        print("\n1. Add  2. Subtract  3. Multiply  4. Divide")
        print("5. Square root  6. Square root of an operation  7. Exit")
        choice = input("Choose (1-7): ")

        if choice == '7':
            print("Goodbye!")
            break

        if choice in ['5', '6']:
            num1, num2 = get_numbers(True) if choice == '5' else get_numbers()
            if choice == '5':
                result = sqrt(num1)
            elif choice == '6':
                op = input("Operation before sqrt (a/b/c/d): ")
                result = operation_before_sqrt(num1, num2, op)
            if result is not None:
                print("Result:", result)
            continue

        num1, num2 = get_numbers()
        result = operations.get(choice)(num1, num2)
        print("Result:", result if result is not None else "Error.")

# Call the calculator function to start the program
calculator()