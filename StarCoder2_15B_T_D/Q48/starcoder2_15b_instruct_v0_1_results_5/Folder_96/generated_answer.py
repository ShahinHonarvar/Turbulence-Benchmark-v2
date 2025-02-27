def return_binary_or_hexa(tup):
    a = tup[50]
    b = tup[200]
    s = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in tup:
            s -= i
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()