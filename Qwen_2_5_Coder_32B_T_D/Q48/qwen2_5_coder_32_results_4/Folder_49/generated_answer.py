def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    s = set(t[80:201])
    ss = sum((i for i in range(a + 1, b) if i not in s))
    if ss == 0:
        return ''
    if ss % 2 == 1:
        return bin(ss)[2:]
    else:
        return hex(ss)[2:]