def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    s = 0
    for i in range(a + 1, b):
        if i not in t[18:61]:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()