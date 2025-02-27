def return_binary_or_hexa(t):
    a, b = (t[20], t[51])
    s = sum((i for i in range(a + 1, b) if i not in t[21:51]))
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:]