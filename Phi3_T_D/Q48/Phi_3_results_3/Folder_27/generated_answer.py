def return_binary_or_hexa(t):
    a, b = (t[86], t[89])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[86:89]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]