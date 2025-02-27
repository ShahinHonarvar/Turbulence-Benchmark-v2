def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    if a + 1 >= b - 1:
        return ''
    total = sum(range(a + 1, b))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()