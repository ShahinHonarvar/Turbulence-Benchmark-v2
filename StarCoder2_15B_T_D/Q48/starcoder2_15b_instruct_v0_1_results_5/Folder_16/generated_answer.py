def return_binary_or_hexa(tup):
    if not isinstance(tup, tuple):
        return ''
    tup = tuple(sorted(set(tup)))
    a = tup[90]
    b = tup[97]
    sum_val = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum_val += i
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()