def return_binary_or_hexa(t):
    a, b = (t[50], t[92])
    s = set(t[50:93])
    sm = sum((i for i in range(a + 1, b) if i not in s))
    if sm:
        return bin(sm)[2:] if sm % 2 else hex(sm)[2:].upper()
    return ''