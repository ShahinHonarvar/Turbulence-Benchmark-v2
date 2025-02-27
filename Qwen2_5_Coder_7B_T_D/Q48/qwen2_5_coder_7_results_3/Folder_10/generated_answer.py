def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[54]
    missing_sum = sum(range(a + 1, b)) - sum(tup[tup.index(a) + 1:tup.index(b)])
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()