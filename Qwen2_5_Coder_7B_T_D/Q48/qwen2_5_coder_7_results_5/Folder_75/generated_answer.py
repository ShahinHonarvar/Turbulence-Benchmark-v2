def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    sum_val = sum((i for i in range(a + 1, b) if i not in t))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]