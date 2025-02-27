def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    missing_sum = sum(range(a + 1, b)) - sum(set(tup[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()