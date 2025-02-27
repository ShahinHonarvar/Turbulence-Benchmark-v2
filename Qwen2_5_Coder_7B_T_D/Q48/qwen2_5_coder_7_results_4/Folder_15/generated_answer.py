def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[4])
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]