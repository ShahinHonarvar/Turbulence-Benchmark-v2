def return_binary_or_hexa(tup):
    a, _, b = tup
    missing_sum = sum(set(range(a + 1, b)) - set(tup))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]