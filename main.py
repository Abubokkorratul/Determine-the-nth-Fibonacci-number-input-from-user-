n = int(input("Enter the position (n) of the Fibonacci number: "))
a, b = 0, 1
if n == 1:
    print("Fibonacci number at position 1 is 0")
elif n == 2:
    print("Fibonacci number at position 2 is 1")
else:
    for _ in range(2, n):
        a, b = b, a + b
    print(f"Fibonacci number at position {n} is {b}")
