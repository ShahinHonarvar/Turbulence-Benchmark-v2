def return_binary_or_hexa(tup):
    a = tup[49]
    b = tup[74]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[49:75]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]