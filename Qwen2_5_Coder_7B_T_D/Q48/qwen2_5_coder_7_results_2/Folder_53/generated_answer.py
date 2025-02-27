def return_binary_or_hexa(t):
    a, b = (t[200], t[202])
    total = sum(range(a + 1, b)) - sum((t[i] for i in range(200, 203) if a + 1 <= t[i] <= b - 1))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()