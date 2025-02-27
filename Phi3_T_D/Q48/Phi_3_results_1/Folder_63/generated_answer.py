def return_binary_or_hexa(tup):
    a = tup[81]
    b = tup[86]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[81:86]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]