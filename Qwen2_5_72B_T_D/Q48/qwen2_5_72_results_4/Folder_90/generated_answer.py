def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[90]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[61:90]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]