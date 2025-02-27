def return_binary_or_hexa(tup):
    a, b = (tup[1], tup[8])
    missing_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(tup.index(a), tup.index(b) + 1)))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()