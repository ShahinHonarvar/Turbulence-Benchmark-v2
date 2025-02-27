def return_binary_or_hexa(tup):
    a = tup[39]
    b = tup[43]
    missing_sum = sum(set(range(a + 1, b)).difference(tup[39:44]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]