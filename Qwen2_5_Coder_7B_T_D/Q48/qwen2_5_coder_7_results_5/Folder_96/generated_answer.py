def return_binary_or_hexa(tup):
    a = tup[50]
    b = tup[200]
    sum_val = sum((i for i in range(a + 1, b) if i not in tup[a + 1:b]))
    if sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]