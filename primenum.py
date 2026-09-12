num = int(input("Enter any num:"))
prime = False
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    else:
        prime = True
if prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")