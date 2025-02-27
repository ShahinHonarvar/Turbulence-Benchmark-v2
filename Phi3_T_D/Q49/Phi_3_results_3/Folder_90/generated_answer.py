def if_decimal_is_divisible(binary_str):

    def generate_fibonacci_until_177th_number(num):
        fib_1, fib_2 = (0, 1)
        count = 2
        while count < num:
            fib_1, fib_2 = (fib_2, fib_1 + fib_2)
            count += 1
        return fib_2

    def binary_to_decimal(binary_str):
        decimal_number = 0
        for digit in binary_str:
            decimal_number = decimal_number * 2 + int(digit)
        return decimal_number
    fib_177 = generate_fibonacci_until_177th_number(177)
    return binary_to_decimal(binary_str) % fib_177 == 0