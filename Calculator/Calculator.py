def add(x,y):
     return x + y
def subtract(x,y):
     return x - y
def multiply(x,y):
     return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Enter 'A' for Addition")
print("Enter 'M' for Multiplication")
print("Enter 'S' for Subtraction")
print("Enter 'D' for Division")

choice = input("Enter Choice (A,M,S,D): ")

while True:

    if choice.upper() in ("A","ADD","ADDITION","S","SUBTRACT","SUBTRACTION","M","MULTIPLY","MULTIPLICATION","D","DIVISION"):
        num1 = float(input("Insert the first number: "))
        num2 = float(input("Insert the second number: "))

    if choice.upper() in ("A","ADDITION","ADD"):
        print("Result: ", num1, "+",num2, "=", add(num1,num2))
    
    elif choice.upper() in ("S","SUBTRACT","SUBTRACTION"):
        print("Result: ", num1, "-",num2, "=", subtract(num1,num2))
              
    elif choice.upper() in ("M","MULTIPLY","MULTIPLICATION"):
        print("Result: ", num1, "*",num2, "=", multiply(num1,num2))
    
    elif choice.upper() in ("D","DIVIDE","DIVISION"):
        print("Result: ", num1, "/",num2, "=", divide(num1,num2))
    else:
        print("Please input the correct choice. ")

    next_calculation = input("Would you like to do another calculation? (yes/no): ")
    if next_calculation.lower() in ("n","nope","no"):
            break
