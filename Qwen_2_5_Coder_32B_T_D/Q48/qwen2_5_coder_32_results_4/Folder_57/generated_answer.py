def return_binary_or_hexa(t):
    a, b = (t[25], t[80])
    s = set(t[25:81])
    total = sum((i for i in range(a + 1, b) if i not in s))
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]