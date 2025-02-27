def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    sum_val = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_val += i
    if sum_val % 2 == 0:
        return hex(sum_val)[2:].upper()
    else:
        return bin(sum_val)[2:]