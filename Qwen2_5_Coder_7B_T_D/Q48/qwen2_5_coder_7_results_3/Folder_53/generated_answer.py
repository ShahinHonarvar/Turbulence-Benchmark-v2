def return_binary_or_hexa(t):
    a = t[200]
    b = t[202]
    sum_val = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    if sum_val % 2 == 0:
        return hex(sum_val)[2:].upper()
    else:
        return bin(sum_val)[2:]