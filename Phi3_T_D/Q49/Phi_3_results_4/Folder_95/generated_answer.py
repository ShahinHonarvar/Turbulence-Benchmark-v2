def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_representation):
    x = binary_to_decimal(binary_representation)
    fib_sequence_index = 167
    fib_number = Fibonacci(fib_sequence_index)
    return x % fib_number == 0