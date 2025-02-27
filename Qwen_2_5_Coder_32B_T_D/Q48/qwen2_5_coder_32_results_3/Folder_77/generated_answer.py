def return_binary_or_hexa(t):
    a, b = (t[18], t[52])
    s = set(t[19:52])
    r = sum((i for i in range(a + 1, b) if i not in s))
    if r == 0:
        return ''
    if r % 2:
        return bin(r)[2:]
    return hex(r)[2:]