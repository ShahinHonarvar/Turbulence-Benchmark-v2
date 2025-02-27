def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    s = 0
    i = a + 1
    j = 39
    while i < b:
        if j < 81 and t[j] == i:
            j += 1
        else:
            s += i
        i += 1
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]