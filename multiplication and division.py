def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

# Test the functions
num1 = float(input("Enter your number: "))
num2 = float(input("Enter your number: "))


# Multiplication
result_multiply = multiply(num1, num2)
print(f"Multiplication of {num1} and {num2} is: {result_multiply}")

# Division
result_divide = divide(num1, num2)
print(f"Division of {num1} by {num2} is: {result_divide}")
