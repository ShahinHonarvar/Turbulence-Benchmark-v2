def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    s = set(t[74:84])
    sm = 0
    for x in range(a + 1, b):
        if x not in s:
            sm += x
    if sm == 0:
        return ''
    if sm % 2 == 1:
        return bin(sm)[2:]
    return hex(sm)[2:]