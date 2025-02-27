def return_binary_or_hexa(tup):
    a = tup[6]
    b = tup[7]
    missing_sum = sum(set(range(a + 1, b)).difference(tup[6:b + 1]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]