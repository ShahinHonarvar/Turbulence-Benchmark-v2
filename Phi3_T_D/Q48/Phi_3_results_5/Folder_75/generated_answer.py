def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[20:52]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]