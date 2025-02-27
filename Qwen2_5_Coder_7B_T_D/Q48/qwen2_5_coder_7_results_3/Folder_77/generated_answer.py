def return_binary_or_hexa(t):
    a = t[18]
    b = t[52]
    sum_val = sum(set(range(a + 1, b)) - set(t[a + 1:b]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()