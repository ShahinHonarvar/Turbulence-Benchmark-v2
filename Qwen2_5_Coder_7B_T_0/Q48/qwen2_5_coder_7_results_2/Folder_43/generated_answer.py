def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    s = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[10:29]]
    if missing:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]