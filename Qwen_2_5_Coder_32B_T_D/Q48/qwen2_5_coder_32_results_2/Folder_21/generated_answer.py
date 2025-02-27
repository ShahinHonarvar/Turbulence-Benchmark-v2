def return_binary_or_hexa(t):
    a, b = (t[15], t[57])
    s = set(t[16:57])
    r = sum((i for i in range(a + 1, b) if i not in s))
    if r == 0:
        return ''
    return bin(r)[2:] if r % 2 else hex(r)[2:]