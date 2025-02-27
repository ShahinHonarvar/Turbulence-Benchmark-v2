def return_binary_or_hexa(t):
    a, b = (t[86], t[89])
    s = sum((x for x in range(a + 1, b) if x not in t[87:89]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]