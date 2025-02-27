def return_binary_or_hexa(tup):
    a, b = (tup[90], tup[200])
    sum_val = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in tup:
            sum_val -= i
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]