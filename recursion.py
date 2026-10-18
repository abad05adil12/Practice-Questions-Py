def ftn(n):
    if n == 0:
        return 0

    return n + ftn(n - 2)


print(ftn(6))