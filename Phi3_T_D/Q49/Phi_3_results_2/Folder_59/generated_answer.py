def fib_up_to_74():
    fib = [0, 1]
    for _ in range(2, 75):
        fib.append(fib[-1] + fib[-2])
    return fib

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def if_decimal_is_divisible(binary_str):
    fib_74 = fib_up_to_74()[74]
    decimal_value = binary_to_decimal(binary_str)
    return decimal_value % fib_74 == 0