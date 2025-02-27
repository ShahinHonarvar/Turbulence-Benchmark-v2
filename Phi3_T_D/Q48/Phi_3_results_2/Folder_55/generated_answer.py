def return_binary_or_hexa(tup):
    a, b = (tup[10], tup[12])
    missing_sum = sum(set(range(a + 1, b)) - set(tup[10:13]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]