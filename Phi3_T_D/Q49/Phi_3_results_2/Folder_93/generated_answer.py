def if_decimal_is_divisible(bin_str):
    fib_59 = [*bin_str_to_decimal(fib_to_bin_str(fibonacci(59)))]
    num_decimal = int(bin_str, 2)
    return num_decimal % fib_59 == 0

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def fib_to_bin_str(n):
    return bin(n)[2:]

def bin_str_to_decimal(bin_str):
    return int(bin_str, 2)