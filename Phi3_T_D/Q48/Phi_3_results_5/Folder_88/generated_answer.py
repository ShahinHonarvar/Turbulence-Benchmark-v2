def return_binary_or_hexa(tup):
    a, b = (tup[3], tup[9])
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[3:10]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]