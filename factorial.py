def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1

for i in range(0, 5):
    print(factorial(i))
