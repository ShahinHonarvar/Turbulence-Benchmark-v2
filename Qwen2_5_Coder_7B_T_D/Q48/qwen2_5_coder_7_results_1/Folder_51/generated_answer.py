def return_binary_or_hexa(t):
    a, b = (t[6], t[9])
    sum_val = sum((i for i in range(a + 1, b) if i not in t[6:10]))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()