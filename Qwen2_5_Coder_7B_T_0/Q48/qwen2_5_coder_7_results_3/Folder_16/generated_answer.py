def return_binary_or_hexa(t):
    a = t[90]
    b = t[97]
    s = sum((i for i in range(a + 1, b) if i not in t[90:98]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()