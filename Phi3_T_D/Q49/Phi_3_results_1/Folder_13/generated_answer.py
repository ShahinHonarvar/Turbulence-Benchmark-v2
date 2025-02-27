def if_decimal_is_divisible(binary_string):
    fib_index = 174
    fib_numbers = [0, 1]
    while len(fib_numbers) <= fib_index:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    fib_174th = fib_numbers[-1]
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_174th == 0