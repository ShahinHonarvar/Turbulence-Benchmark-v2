def if_decimal_is_divisible(binary_str):

    def is_fib_divisible_by_n(n):
        if n == 0:
            return True
        a, b = (0, 1)
        fib_nth = n
        while b < fib_nth:
            a, b = (b, a + b)
        return b == fib_nth
    decimal_num = int(binary_str, 2)
    fibonacci_ninety = 34
    return is_fib_divisible_by_n(fibonacci_ninety) if decimal_num % fibonacci_ninety == 0 else False