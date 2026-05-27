# Task 2: Calculator Application

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("\n--- PYTHON CALCULATOR ---")
    
    try:
        # Taking inputs from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    print("\nChoose Operation:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    
    choice = input("\nEnter choice (+, -, *, /): ")

    # Operations using if-else logic
    if choice == '+':
        print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '-':
        print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '*':
        print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '/':
        print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Operation choice!")

# Run the calculator
if __name__ == "__main__":
    while True:
        calculator()
        next_calc = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if next_calc != 'yes':
            print("Thank you for using Python Calculator. Goodbye!")
            break
