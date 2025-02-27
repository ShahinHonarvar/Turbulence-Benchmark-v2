def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    s = set(t[18:61])
    r = sum((i for i in range(a + 1, b) if i not in s))
    if r == 0:
        return ''
    elif r % 2 == 1:
        return bin(r)[2:]
    else:
        return hex(r)[2:]