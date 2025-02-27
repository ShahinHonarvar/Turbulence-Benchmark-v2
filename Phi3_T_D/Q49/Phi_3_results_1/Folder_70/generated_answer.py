def if_decimal_is_divisible(bin_str):

    def fibo_137():
        a, b, counter = (0, 1, 1)
        while counter <= 137:
            a, b = (b, a + b)
            counter += 1
        return a
    decimal_value = int(bin_str, 2)
    return decimal_value % fibo_137() == 0