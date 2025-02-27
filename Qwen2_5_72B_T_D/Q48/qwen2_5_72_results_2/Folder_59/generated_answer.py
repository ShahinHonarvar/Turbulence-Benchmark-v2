def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[10])
    missing_sum = sum(set(range(a + 1, b)) - set(tup[1:10]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]