fact=5
for i in range(fact + 1):
    if i == 0:
        fact = 1
    else:
        fact *= i

    print(f"Factorial of {i} is {fact}")