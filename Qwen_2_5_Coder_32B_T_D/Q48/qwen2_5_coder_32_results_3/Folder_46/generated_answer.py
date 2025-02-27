def return_binary_or_hexa(t):
    a, b = (t[10], t[79])
    s = set(t[10:80])
    total = 0
    for num in range(a + 1, b):
        if num not in s:
            total += num
    if total % 2:
        return bin(total)[2:]
    elif total:
        return hex(total)[2:]
    return ''