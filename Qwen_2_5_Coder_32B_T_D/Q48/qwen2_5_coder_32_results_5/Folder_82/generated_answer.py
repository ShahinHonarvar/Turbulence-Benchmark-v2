def return_binary_or_hexa(t):
    a, b = (t[20], t[200])
    s = 0
    check_set = set(t[21:200])
    for i in range(a + 1, b):
        if i not in check_set:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]