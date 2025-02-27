def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[8])
    total_sum = sum((i for i in range(a + 1, b) if i not in tup))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]