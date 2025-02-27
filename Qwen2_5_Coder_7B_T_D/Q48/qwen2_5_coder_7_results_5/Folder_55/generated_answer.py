def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    sum_val = sum(range(a + 1, b))
    present = any((t[i] in range(a + 1, b) for i in range(10, 13)))
    if present:
        return ''
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()