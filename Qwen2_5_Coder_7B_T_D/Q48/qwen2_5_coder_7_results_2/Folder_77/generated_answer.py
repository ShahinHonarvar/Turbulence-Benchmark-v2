def return_binary_or_hexa(t):
    a, b = (t[18], t[52])
    if a >= b:
        return ''
    missing_sum = sum(set(range(a + 1, b)) - set(t[a + 1:b]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()