def return_binary_or_hexa(t):
    a, b = (t[20], t[35])
    s = sum(range(a + 1, b)) - sum(filter(lambda x: x > a and x < b, t[20:36]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()