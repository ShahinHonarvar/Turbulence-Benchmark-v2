def if_decimal_is_divisible(binary_str):

    def dec_from_binary(bin_str):
        return int(bin_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    dec_num = dec_from_binary(binary_str)
    tenth_fibonacci = fibonacci(10)
    return dec_num % tenth_fibonacci == 0