def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    full_set = set(range(a + 1, b))
    present_set = set(t[91:97])
    missing_set = full_set - present_set
    s = sum(missing_set)
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]