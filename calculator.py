print("Welcome to the Python Calculator!")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")

choice_1 = input("Enter your number: ")
choice_2 = input("Enter your number: ")
def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y

if choice_1 == '' and choice_2 == '':
    print("Invalid input. Please select 1 or 2.")
else:
    # Get numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sum = addition(x=num1,y=num2)
    difference = substraction(x=num1,y=num2)

    print(f"sum of {choice_1} and {choice_2} = {sum}")
    print(f"difference of {choice_1} and {choice_2} = {difference}")