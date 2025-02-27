def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    s = set(t[42:88])
    total = sum((x for x in range(a + 1, b) if x not in s))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]