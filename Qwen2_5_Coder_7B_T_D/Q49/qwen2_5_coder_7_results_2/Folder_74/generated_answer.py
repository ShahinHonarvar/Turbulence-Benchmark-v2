def if_decimal_is_divisible(binary_str):
    fibo_seq = [0, 1]
    for i in range(2, 166):
        fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
    dec_value = int(binary_str, 2)
    return dec_value % fibo_seq[165] == 0