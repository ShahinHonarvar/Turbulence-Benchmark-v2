def return_binary_or_hexa(t):
    a, b = (t[68], t[99])
    total = sum(range(a + 1, b)) - sum((t[i] for i in range(69, 100)))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()