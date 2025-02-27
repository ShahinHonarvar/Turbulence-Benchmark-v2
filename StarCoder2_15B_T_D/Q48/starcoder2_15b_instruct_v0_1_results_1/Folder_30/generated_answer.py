def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    sum_val = 0
    for i in range(a + 1, b):
        if i not in t:
            sum_val += i
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()