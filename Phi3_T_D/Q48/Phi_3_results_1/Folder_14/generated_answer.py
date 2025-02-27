def return_binary_or_hexa(t):
    a = t[2]
    b = t[5]
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[2:5]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]