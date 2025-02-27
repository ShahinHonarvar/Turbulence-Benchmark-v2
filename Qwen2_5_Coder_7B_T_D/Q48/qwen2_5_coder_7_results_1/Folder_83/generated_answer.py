def return_binary_or_hexa(t):
    a, b = (t[90], t[200])
    s = sum(range(a + 1, b) - set(t[90:201]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()