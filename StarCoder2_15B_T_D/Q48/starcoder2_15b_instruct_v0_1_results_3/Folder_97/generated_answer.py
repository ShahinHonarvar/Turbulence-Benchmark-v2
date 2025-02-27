def return_binary_or_hexa(t):
    a, b = (t[34], t[69])
    s = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in t:
            s -= i
    if s % 2 == 1:
        return bin(s)[2:]
    elif s != 0:
        return hex(s)[2:]
    else:
        return ''