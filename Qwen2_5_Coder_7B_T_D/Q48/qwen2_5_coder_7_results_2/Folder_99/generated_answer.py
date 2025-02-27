def return_binary_or_hexa(t):
    a, b = (t[427], t[669])
    s = sum(range(a + 1, b))
    if all((x not in range(a + 1, b) for x in t[427:670])):
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()