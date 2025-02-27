def if_decimal_is_divisible(binary_str):
    fib_178 = 0
    fib_177 = 1
    fib_179 = 1
    for i in range(177):
        fib_179, fib_178, fib_177 = (fib_178 + fib_179, fib_179, fib_178)
    fib_178 = fib_178 % 1000000007
    decimal = int(binary_str, 2)
    return decimal % fib_178 == 0