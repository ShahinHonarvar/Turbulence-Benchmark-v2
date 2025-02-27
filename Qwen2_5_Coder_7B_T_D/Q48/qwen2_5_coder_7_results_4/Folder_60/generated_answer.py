def return_binary_or_hexa(t):
    a = t[38]
    b = t[52]
    sum_val = sum((i for i in range(a + 1, b) if i not in t[a:b + 1]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()