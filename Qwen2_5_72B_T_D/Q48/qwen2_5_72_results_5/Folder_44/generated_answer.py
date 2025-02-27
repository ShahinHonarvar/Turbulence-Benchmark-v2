def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[52]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[37:52]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]