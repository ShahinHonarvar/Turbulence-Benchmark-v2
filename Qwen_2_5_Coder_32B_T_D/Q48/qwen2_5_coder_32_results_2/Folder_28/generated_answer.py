def return_binary_or_hexa(t):
    a = t[86]
    b = t[99]
    s = 0
    for x in range(a + 1, b):
        if x not in t[87:100]:
            s += x
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:]
    return ''