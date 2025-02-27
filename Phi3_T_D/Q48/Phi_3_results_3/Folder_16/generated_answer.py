def return_binary_or_hexa(t):
    a, b = (t[90], t[97])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[90:97]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]