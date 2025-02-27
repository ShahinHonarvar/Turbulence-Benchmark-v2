def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    s = 0
    current = a + 1
    i = 69
    while current < b:
        if i < 99 and t[i] == current:
            i += 1
        else:
            s += current
        current += 1
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]