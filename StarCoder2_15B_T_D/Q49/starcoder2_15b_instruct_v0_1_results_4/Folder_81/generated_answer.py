def if_decimal_is_divisible(binary_string):
    decimal_integer = 0
    for i, digit in enumerate(binary_string):
        decimal_integer += int(digit) * 2 ** (len(binary_string) - 1 - i)
    fib = [0, 1]
    for i in range(2, 97):
        fib.append(fib[i - 1] + fib[i - 2])
    for fib_number in fib:
        if fib_number >= decimal_integer:
            break
    return decimal_integer % fib_number == 0