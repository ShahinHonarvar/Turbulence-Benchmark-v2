def if_decimal_is_divisible(binary_string):

    def fib_index(n):
        a, b, counter = (0, 1, 1)
        while counter < n:
            a, b = (b, a + b)
            counter += 1
        return b

    def binary_to_decimal(binary_string):
        return int(binary_string, 2)
    fib_160th = fib_index(160)
    decimal_number = binary_to_decimal(binary_string)
    return decimal_number % fib_160th == 0