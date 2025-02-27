def return_binary_or_hexa(t):
    a, b = (t[32], t[44])
    missing_sum = sum(set(range(a + 1, b)) - set(t[32:45]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]