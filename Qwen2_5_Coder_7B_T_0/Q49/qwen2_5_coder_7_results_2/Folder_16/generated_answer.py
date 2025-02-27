def if_decimal_is_divisible(binary_str):
    fib_128 = 2178309227425801075748064194580822283
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_128 == 0