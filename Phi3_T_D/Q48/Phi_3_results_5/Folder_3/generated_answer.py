def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[56:88]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]