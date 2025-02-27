def return_binary_or_hexa(t):
    a, b = (t[19], t[32])
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[19:32]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()