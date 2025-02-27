def return_binary_or_hexa(t):
    a, _, _, _, _, _, b = t
    missing_sum = sum(set(range(a + 1, b)) - set(t))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]