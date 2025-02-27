def return_binary_or_hexa(tup):
    a, b, _, _, _, _ = tup
    sum_val = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_val += i
    if sum_val % 2 == 1:
        return bin(sum_val).replace('0b', '')
    else:
        return hex(sum_val).replace('0x', '')