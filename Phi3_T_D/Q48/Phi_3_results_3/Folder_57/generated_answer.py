def return_binary_or_hexa(tup):
    a = tup[25]
    b = tup[80]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[25:80]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]