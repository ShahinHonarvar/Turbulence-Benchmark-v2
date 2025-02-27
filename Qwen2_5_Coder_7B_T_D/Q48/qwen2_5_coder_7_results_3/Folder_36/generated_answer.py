def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[110:349]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()