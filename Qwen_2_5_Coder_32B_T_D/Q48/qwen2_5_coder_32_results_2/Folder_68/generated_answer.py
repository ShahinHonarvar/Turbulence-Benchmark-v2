def return_binary_or_hexa(t):
    a, *_, b = t
    s = 0
    for i in range(a + 1, b):
        if i not in t:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]