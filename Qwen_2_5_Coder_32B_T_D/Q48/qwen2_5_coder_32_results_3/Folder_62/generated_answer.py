def return_binary_or_hexa(t):
    a, b = (t[50], t[92])
    s = set(t[51:92])
    total = sum((i for i in range(a + 1, b) if i not in s))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]