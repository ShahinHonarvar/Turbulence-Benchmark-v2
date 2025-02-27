def return_binary_or_hexa(t):
    a, b = (t[49], t[74])
    s = 0
    for i in range(a + 1, b):
        if i not in t[49:75]:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]