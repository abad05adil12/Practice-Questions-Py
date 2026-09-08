def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Division by zero is not allowed"
    else:
        return a/b
    
    
while True:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    
    print("1. Addition")
    print("\n2. Subtraction")
    print("\n3. Multiplication")
    print("\n4. Division")
    print("\n5. Exit")
    
    choice=int(input("Enter your choice:"))
    
    if choice==1:
        print(f"Addition of {a} and {b} is: {add(a,b)}")
    elif choice==2:
        print(f"Subtraction of {a} and {b} is: {sub(a,b)}")
    elif choice==3:
        print(f"Multiplication of {a} and {b} is: {mul(a,b)}")
    elif choice==4:
        print(f"Division of {a} and {b} is: {div(a,b)}")
    elif choice==5:
        print("Exiting the program.")
        break