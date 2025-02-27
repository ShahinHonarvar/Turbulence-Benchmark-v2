def if_decimal_is_divisible(binary_str):

    def is_fibonacci(n):
        a, b = (0, 1)
        while b < n:
            a, b = (b, a + b)
        return b == n

    def fibonacci_index(n):
        a, b = (0, 1)
        index = 0
        while b < n:
            a, b = (b, a + b)
            index += 1
        return index if b == n else -1
    n = int(binary_str, 2)
    fib_9th_index = fibonacci_index(9)
    fib_9th_number = 0 if fib_9th_index == -1 else is_fibonacci(n)
    return fib_9th_number % 9 == 0