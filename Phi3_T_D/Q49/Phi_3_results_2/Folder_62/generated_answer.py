def if_decimal_is_divisible(bin_str):

    def fib_modulo_130():
        fib_mod, prev_mod = (0, 1)
        for _ in range(130):
            fib_mod, prev_mod = ((fib_mod + prev_mod) % 10 ** 9, fib_mod)
        return fib_mod
    num = int(bin_str, 2)
    div = fib_modulo_130()
    return num % div == 0