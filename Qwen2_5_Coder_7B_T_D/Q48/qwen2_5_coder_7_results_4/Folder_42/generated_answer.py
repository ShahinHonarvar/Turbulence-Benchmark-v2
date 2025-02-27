def return_binary_or_hexa(tup):
    a = tup[18]
    b = tup[60]
    total = sum(range(a + 1, b))
    missing_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(tup.index(a) + 1, tup.index(b))))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()