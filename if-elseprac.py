def hello():
    print("Hello, World!")

def bye():
    print("Goodbye, World!")
    
def cont():
    print("Continue, World!")
    

while True:
    input1 = input("Enter your choice (hello/bye/cont): ")
    if input1== "hello":
        hello()
    elif input1=="bye":
        bye()
    elif input1=="cont":
        cont()
    elif input1=="exit":
        print("Exiting the program.")
        break
    else:
        print("invalid choice. Please try again.")
    
    