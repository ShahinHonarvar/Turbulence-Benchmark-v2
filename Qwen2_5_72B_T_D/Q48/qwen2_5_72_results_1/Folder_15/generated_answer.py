def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[4]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[1:4]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]