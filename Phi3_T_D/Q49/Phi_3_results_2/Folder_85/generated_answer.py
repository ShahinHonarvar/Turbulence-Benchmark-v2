def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_numbers = [0, 1]
    a, b = (0, 1)
    while len(fib_numbers) <= 45:
        a, b = (b, a + b)
        fib_numbers.append(b)
    return decimal % fib_numbers[45] == 0