def return_binary_or_hexa(t):
    a = t[70]
    b = t[98]
    s = 0
    m = set(t[71:98])
    for i in range(a + 1, b):
        if i not in m:
            s += i
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]