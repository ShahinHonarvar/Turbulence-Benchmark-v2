def return_binary_or_hexa(t):
    a, b = (t[36], t[85])
    s = sum((i for i in range(a + 1, b) if i not in set(t[t.index(a):t.index(b) + 1])))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()