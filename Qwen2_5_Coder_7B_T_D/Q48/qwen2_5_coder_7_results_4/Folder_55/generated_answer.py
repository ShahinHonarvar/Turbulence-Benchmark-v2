def return_binary_or_hexa(t):
    a, b = (t[10], t[12])
    sum_val = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()