def return_binary_or_hexa(t):
    a, _, _, _, _, _, _, _, b = t
    s = set(t)
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total:
        return bin(total)[2:] if total % 2 else hex(total)[2:]
    return ''