def return_binary_or_hexa(tup):
    a = tup[48]
    b = tup[76]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[49:76]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]