def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[9]
    missing_sum = sum(set(range(a + 1, b)) - set(tup))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()