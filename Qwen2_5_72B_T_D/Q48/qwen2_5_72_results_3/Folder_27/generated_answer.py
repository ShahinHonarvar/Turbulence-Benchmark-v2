def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[87:89]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()