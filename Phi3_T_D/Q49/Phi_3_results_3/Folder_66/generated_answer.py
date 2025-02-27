def if_decimal_is_divisible(binary_string):

    def golden_ratio_fib(n):
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int(round(golden_ratio ** n / 5 ** 0.5))

    def fibonacci_120th_number():
        return golden_ratio_fib(120)
    fib_120 = fibonacci_120th_number()
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_120 == 0