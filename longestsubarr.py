numbers = [1, 2, 1, 1, 1, 3, 2]
target = 3

longest = 0

for i in range(len(numbers)):
    total = 0

    for j in range(i, len(numbers)):
        total += numbers[j]

        if total == target:
            length = j - i + 1

            if length > longest:
                longest = length

print("Longest length:", longest)