def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()