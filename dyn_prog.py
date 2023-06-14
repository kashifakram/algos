def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_table = [0] * (n + 1)
        fib_table[0] = 0
        fib_table[1] = 1

        for i in range(2, n + 1):
            fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

        return fib_table[n]