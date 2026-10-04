numbers = [10, 5, 8, 20, 15]

largest = numbers[0]
second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Largest:", largest)
print("Second largest:", second)