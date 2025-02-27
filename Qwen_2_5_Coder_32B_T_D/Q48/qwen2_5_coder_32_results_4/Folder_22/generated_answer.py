def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    s = set(t[41:200])
    total = 0
    for n in range(a + 1, b):
        if n not in s:
            total += n
    if total:
        return bin(total)[2:] if total % 2 else hex(total)[2:]
    return ''