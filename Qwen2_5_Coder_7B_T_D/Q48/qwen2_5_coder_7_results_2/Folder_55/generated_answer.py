def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    if b - a <= 2:
        return ''
    sum_val = sum((i for i in range(a + 1, b) if i not in t))
    if sum_val % 2 == 0:
        return hex(sum_val)[2:].upper()
    else:
        return bin(sum_val)[2:]