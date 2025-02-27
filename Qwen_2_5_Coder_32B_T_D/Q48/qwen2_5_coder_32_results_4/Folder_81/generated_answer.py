def return_binary_or_hexa(t):
    a, b = (t[10], t[100])
    s = set(t[11:100])
    total = sum((x for x in range(a + 1, b) if x not in s))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]