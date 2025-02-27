def if_decimal_is_divisible(binary_str):
    fibo = [0, 1]
    while len(fibo) <= 185:
        fibo.append(fibo[-1] + fibo[-2])
    decimal = int(binary_str, 2)
    return decimal % fibo[185] == 0