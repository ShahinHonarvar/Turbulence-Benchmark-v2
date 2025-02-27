def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    total = sum(range(a + 1, b)) - sum(set((t[i] for i in range(10, 29))))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()