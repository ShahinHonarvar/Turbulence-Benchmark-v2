def return_binary_or_hexa(tup):
    a, b = (tup[56], tup[88])
    missing_sum = sum(set(range(a + 1, b)).difference(tup[56:88 + 1]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]