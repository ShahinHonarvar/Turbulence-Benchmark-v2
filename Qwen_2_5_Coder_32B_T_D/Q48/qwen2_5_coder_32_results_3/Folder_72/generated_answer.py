def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    s = 0
    p = set(t[14:70])
    for i in range(a + 1, b):
        if i not in p:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]