def find_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


answer = find_sum(5)

print(answer)