def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    s = set(t[45:67])
    sum_val = sum((i for i in range(a + 1, b) if i not in s))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()