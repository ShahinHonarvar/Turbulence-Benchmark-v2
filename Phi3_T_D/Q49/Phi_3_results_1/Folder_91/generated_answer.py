def if_decimal_is_divisible(binary_str):

    def dec_from_binary(binary_str):
        decimal_val = 0
        for digit in binary_str:
            decimal_val = decimal_val * 2 + int(digit)
        return decimal_val

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    decimal_val = dec_from_binary(binary_str)
    sixth_fibonacci = fib(5)
    return decimal_val % sixth_fibonacci == 0