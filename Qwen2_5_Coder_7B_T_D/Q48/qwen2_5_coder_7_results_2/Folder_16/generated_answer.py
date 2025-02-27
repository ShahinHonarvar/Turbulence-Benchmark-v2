def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    s = sum(range(a + 1, b))
    missing = [x for x in range(a + 1, b) if x not in t[90:98]]
    if missing:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]