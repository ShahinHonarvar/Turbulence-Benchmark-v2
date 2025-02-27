def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    s = 0
    for i in range(a + 1, b):
        if i not in t[17:87]:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()