def return_binary_or_hexa(tup):
    a, b = (tup[6], tup[9])
    missing_sum = sum((x for x in range(a + 1, b) if x not in tup[6:10]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]