from functools import reduce

def if_decimal_is_divisible(binary_str):
    fib_198 = reduce(lambda x, _: (x[1], (x[0] + x[1]) % 198), range(198), (0, 1))[0]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_198 == 0