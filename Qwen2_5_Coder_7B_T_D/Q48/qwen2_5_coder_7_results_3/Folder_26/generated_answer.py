def return_binary_or_hexa(tup):
    a = tup[68]
    b = tup[99]
    missing_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(69, 100)))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]