def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    s = 0
    for i in range(a + 1, b):
        if i not in t[33:99]:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]