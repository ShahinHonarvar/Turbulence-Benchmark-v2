def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[2:7]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]