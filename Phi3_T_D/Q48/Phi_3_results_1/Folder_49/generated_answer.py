def return_binary_or_hexa(tup):
    a = tup[80]
    b = tup[200]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[80:200]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]