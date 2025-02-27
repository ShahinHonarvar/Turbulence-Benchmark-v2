def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    s = 0
    p = set(t[934:996])
    for i in range(a + 1, b):
        if i not in p:
            s += i
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]