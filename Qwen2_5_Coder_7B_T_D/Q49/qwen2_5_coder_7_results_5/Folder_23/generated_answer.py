def if_decimal_is_divisible(binary_str):
    fib_48 = 7540113804746346625
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_48 == 0