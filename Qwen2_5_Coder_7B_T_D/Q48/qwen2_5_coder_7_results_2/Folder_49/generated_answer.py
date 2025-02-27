def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    sum_val = sum((i for i in range(a + 1, b) if i not in t[80:201]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()