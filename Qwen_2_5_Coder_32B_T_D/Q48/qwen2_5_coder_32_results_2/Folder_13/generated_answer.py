def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    s = 0
    j = 47
    for i in range(a + 1, b):
        while j < 91 and t[j] < i:
            j += 1
        if j >= 91 or t[j] > i:
            s += i
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()