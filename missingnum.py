numbers = [1, 2, 3, 5, 6]
n = 6

expected = n * (n + 1) // 2
actual = 0

for num in numbers:
    actual += num

missing = expected - actual
print("Missing number:", missing)