def return_binary_or_hexa(tup):
    a, b = (tup[60], tup[90])
    total_sum = sum(range(a + 1, b))
    missing_sum = total_sum - sum((tup[i] for i in range(61, 90)))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()