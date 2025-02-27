def return_binary_or_hexa(t):
    if len(t) < 98:
        return ''
    a = t[69]
    b = t[97]
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[69:97]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]