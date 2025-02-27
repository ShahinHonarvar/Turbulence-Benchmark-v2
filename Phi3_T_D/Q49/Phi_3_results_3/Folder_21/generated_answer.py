def if_decimal_is_divisible(binary_str):
    fibonacci_195 = fibonacci_sequence()[194]
    decimal_int = int(binary_str, 2)
    return decimal_int % fibonacci_195 == 0

def fibonacci_sequence(n=200):
    fib_numbers = [0, 1]
    for i in range(2, n):
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_fib)
    return fib_numbers