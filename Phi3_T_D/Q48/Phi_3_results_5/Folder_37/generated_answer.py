def return_binary_or_hexa(t):
    a, _, _, _, _, _, b, *_ = t
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[2:7]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]