def return_binary_or_hexa(tup):
    a = tup[32]
    b = tup[44]
    missing_sum = sum((x for x in range(a + 1, b) if x not in tup[32:45]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]