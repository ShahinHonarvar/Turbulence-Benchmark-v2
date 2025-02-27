def return_binary_or_hexa(t):
    a, b = (t[50], t[200])
    s = set(t[51:200])
    u = sum((i for i in range(a + 1, b) if i not in s))
    if u:
        return bin(u)[2:] if u % 2 else hex(u)[2:]
    return ''