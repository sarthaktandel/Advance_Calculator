import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error! Cannot compute the square root of a negative number."
    else:
        return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def menu():
    print("\nAdvanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice (1-10): ")
        
        if choice == '10':
            print("Successfully Exited!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '6':
            num = float(input("Enter number: "))
            print(f"Result: √{num} = {sqrt(num)}")
        elif choice == '7':
            num = float(input("Enter angle in degrees: "))
            print(f"Result: sin({num}) = {sin(num)}")
        elif choice == '8':
            num = float(input("Enter angle in degrees: "))
            print(f"Result: cos({num}) = {cos(num)}")
        elif choice == '9':
            num = float(input("Enter angle in degrees: "))
            print(f"Result: tan({num}) = {tan(num)}")
        else:
            print("Invalid Input\nTry Again")

if __name__ == "__main__":
    main()