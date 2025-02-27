def fibonacci_99():
    fib_seq = [0, 1, 1]
    while len(fib_seq) < 99:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[-1]

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    decimal = binary_to_decimal(binary_str)
    fib_99th = fibonacci_99()
    return decimal % fib_99th == 0