def if_decimal_is_divisible(binary_str):
    fib_128 = 25844174676256268734074684517659435921
    decimal = int(binary_str, 2)
    return decimal % fib_128 == 0