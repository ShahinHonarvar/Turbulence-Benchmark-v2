def return_binary_or_hexa(tuple):
    a, b = (tuple[56], tuple[90])
    missing_sum = sum(set(range(a + 1, b)).difference(set(tuple[56:90 + 1])))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]