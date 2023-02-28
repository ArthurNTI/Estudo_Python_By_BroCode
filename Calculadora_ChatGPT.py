import math

# Define functions for different mathematical operations

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

def power(num1, num2):
    return num1 ** num2

def square_root(num):
    if num < 0:
        return "Cannot calculate square root of a negative number"
    else:
        return math.sqrt(num)

def sin(num):
    return math.sin(num)

def cos(num):
    return math.cos(num)

def tan(num):
    return math.tan(num)

# Main program loop

while True:
    # Display the available operations
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("0. Exit")

    # Take user input for operation choice
    choice = input("Enter operation choice: ")

    # Exit the program if the user enters 0
    if choice == "0":
        print("Exiting calculator...")
        break

    # Take user input for numbers to perform calculation on
    num1 = float(input("Enter first number: "))
    if choice != "6" and choice != "7" and choice != "8" and choice != "9":
        num2 = float(input("Enter second number: "))

    # Perform the chosen operation and output the result
    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    elif choice == "5":
        result = power(num1, num2)
    elif choice == "6":
        result = square_root(num1)
    elif choice == "7":
        result = sin(num1)
    elif choice == "8":
        result = cos(num1)
    elif choice == "9":
        result = tan(num1)
    else:
        print("Invalid operation")
        continue

    print("Result: ", result)
