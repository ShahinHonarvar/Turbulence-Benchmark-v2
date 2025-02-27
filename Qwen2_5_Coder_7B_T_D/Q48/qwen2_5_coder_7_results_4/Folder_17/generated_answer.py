def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[73:85]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()