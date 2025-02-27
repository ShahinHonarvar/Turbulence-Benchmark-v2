def return_binary_or_hexa(tup):
    a, b = (tup[56], tup[90])
    missing_sum = sum(set(range(a + 1, b)) - set(tup[56:90]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]