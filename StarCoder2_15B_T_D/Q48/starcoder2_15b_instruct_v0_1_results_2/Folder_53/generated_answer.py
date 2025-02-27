def return_binary_or_hexa(tup):
    a = tup[200]
    b = tup[202]
    sum_val = sum(range(a + 1, b))
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].upper()