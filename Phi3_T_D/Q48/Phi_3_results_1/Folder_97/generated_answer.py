def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[34:69 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]