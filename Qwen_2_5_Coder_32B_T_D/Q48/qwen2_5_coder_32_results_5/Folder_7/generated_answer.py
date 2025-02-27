def return_binary_or_hexa(t):
    a, b = (t[10], t[97])
    s = set(t[11:97])
    total = 0
    for i in range(a + 1, b):
        if i not in s:
            total += i
    if total:
        return bin(total)[2:] if total % 2 else hex(total)[2:]
    return ''