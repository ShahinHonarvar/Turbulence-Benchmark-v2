def return_binary_or_hexa(t):
    a, b = (t[1], t[8])
    missing_sum = sum(range(a + 1, b)) - sum((i for i in range(a + 1, b) if i in t[1:8]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()