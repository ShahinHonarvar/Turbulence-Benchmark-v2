def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    s = 0
    for i in range(a + 1, b):
        if i not in t[73:93]:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]