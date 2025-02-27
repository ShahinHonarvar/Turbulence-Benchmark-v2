def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    required_sum = sum(range(a + 1, b))
    missing_sum = sum(set(range(a + 1, b)) - set(tup[10:80]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]