def return_binary_or_hexa(t):
    a, b = (t[60], t[200])
    s, x = (set(t[60:201]), 0)
    for i in range(a + 1, b):
        if i not in s:
            x += i
    if x == 0:
        return ''
    elif x % 2 == 1:
        return bin(x)[2:]
    else:
        return hex(x)[2:].upper()