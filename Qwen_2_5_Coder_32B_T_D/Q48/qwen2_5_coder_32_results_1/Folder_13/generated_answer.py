def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[47:91]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]