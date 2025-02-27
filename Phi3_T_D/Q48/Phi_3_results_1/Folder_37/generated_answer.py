def return_binary_or_hexa(tup):
    a, b = (tup[2], tup[7])
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[2:7]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]