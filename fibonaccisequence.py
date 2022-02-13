def fibonacci_number(n):
    a = 0
    b = 1
    fib = [a, b]

    for i in range(n):
        f = a + b
        a = b
        b = f
        fib.append(f)
    print(f"{fib}")


fibonacci_number(10)
