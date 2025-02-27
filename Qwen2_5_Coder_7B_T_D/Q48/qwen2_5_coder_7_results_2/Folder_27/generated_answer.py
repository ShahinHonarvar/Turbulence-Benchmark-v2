def return_binary_or_hexa(t):
    a = t[86]
    b = t[89]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]