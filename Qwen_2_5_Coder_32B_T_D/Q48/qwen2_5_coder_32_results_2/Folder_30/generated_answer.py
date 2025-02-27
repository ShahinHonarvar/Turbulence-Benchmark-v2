def return_binary_or_hexa(t):
    a, b = (t[22], t[24])
    s = 0
    for i in range(a + 1, b):
        if i not in t[23:24]:
            s += i
    if s % 2 == 1:
        return bin(s)[2:]
    elif s % 2 == 0 and s != 0:
        return hex(s)[2:]
    return ''