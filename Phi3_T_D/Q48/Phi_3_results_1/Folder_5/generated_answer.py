def return_binary_or_hexa(t):
    a = t[2]
    b = t[8]
    sum_missing = sum(set(range(a + 1, b)).difference(set(t[2:8])))
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]