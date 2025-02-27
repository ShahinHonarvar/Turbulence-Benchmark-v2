from math import log2

def fib_mod_n(n):
    fib_mods = [0, 1]
    for i in range(2, n + 1):
        fib_mods.append((fib_mods[-1] + fib_mods[-2]) % n)
    return fib_mods

def if_decimal_is_divisible(bin_str):
    n = int(bin_str, 2)
    fib_189_mod = fib_mod_n(189)[-1]
    return n % fib_189_mod == 0