def return_binary_or_hexa(t):
    a, _, _, _, _, _, _, _, _, _, b, _ = t
    missing_sum = sum(set(range(a + 1, b)) - set(t[10:13]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]