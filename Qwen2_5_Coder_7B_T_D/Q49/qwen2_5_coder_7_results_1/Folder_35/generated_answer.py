def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 188):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    fib_187 = fibonacci[187]
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_187 == 0