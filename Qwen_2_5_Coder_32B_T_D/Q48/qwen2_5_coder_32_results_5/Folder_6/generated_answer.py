def return_binary_or_hexa(t):
    a, b = (t[20], t[93])
    s = set(t[20:94])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total:
        return bin(total)[2:] if total % 2 else hex(total)[2:]
    return ''