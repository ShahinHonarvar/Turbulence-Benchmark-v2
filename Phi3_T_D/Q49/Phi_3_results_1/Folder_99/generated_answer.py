from sympy import isprime

def if_decimal_is_divisible(bin_str):
    fibo_seq = [0, 1]
    while len(fibo_seq) < 109:
        next_val = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(next_val)
    divisor = fibo_seq[-1]
    decimal_number = int(bin_str, 2)
    return decimal_number % divisor == 0