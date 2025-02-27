def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[200]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[91:200]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]