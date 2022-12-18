def multiply(m1, m2):
    print("The answer is:", m1*m2)

def divide(d1, d2):
    print("The answer is: ", d1/d2)

def add(a1, a2):
    print("The answer is: ", a1+a2)

def sub(s1, s2):
    print("The answer is: ", s1-s2)

choice = input("Choose what kind of action you wish to perform. M to Multiply, D to divide, S to subtract, or S to add:")

if choice == "M":
    print("You have chosen to multiply.")
    m1 = int(input("Enter the first number to multiply: "))
    m2 = int(input("Enter the second number to multiply: "))
    multiply(m1,m2)

if choice == "D":
    print("You have chosen to divide.")
    d1 = int(input("Enter the number you want to be divded: "))
    d2 = int(input("Enter the number that divdes the first: "))
    divide(d1,d2)

if choice == "A":
    print("You have chosen to addd.")
    a1 = int(input("Enter the first addend: "))
    a2 = int(input("Enter the second addend: "))
    add(a1,a2)

if choice == "s":
    print("You have chosen to subtract.")
    s1 = int(input("Enter the number you want to subtract: "))
    s2 = int(input("Enter the number that subtracts the first: "))
    subtract(s1,s2)
