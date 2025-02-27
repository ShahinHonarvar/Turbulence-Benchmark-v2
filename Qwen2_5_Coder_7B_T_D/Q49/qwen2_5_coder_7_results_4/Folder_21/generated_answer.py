def if_decimal_is_divisible(binary_str):
    fib_195 = 4807526976838840674651110466628817034554436098742942744073709551615
    decimal = int(binary_str, 2)
    return decimal % fib_195 == 0