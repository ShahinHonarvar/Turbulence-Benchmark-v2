def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    s = 0
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in t[18:88]:
            missing_sum += i
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    elif missing_sum:
        return hex(missing_sum)[2:]
    return ''