def if_decimal_is_divisible(binary_str):
    fib_numbers = [0, 1]
    for i in range(2, 7):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    decimal = int(binary_str, 2)
    return decimal % fib_numbers[6] == 0