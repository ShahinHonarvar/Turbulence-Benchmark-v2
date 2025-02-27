def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    s = 0
    for i in range(a + 1, b):
        if i not in t[49:75]:
            s += i
    if s % 2:
        return bin(s)[2:]
    elif s:
        return hex(s)[2:]
    else:
        return ''