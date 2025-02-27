def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < 178:
        next_fib = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_fib)
    return decimal_number % fibonacci_seq[-1] == 0