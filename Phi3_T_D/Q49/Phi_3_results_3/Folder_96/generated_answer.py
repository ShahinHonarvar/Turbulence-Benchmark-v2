def if_decimal_is_divisible(binary_string):
    fib_47 = fibonacci(47)
    decimal = int(binary_string, 2)
    return decimal % fib_47 == 0

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]