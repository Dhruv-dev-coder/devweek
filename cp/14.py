def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
# Example of using the generator
for num in fibonacci(5):
    print(num, end=" ")
print("Project by DHRUV GUPTA, 2024UC18045")
