from enum import IntEnum

def if_decimal_is_divisible(binary):

    class Fibonacci(IntEnum):
        ZERO = 0
        ONE = 1

    def fibonacci(n):
        if n <= Fibonacci.FIVE.value:
            return n
        previous, current = (Fibonacci.ONE.value, Fibonacci.ZERO.value)
        for _ in range(2, n + 1):
            previous, current = (current, previous + current)
        return current

    def binary_to_decimal(binary_str):
        decimal = 0
        for digit in binary_str:
            decimal = decimal * 2 + int(digit)
        return decimal
    decimal = binary_to_decimal(binary)
    fib_190 = fibonacci(190)
    return decimal % fib_190 == 0