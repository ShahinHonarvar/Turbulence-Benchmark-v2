def return_binary_or_hexa(t):
    a, b = (t[34], t[69])
    total = 0
    for i in range(a + 1, b):
        if i not in t:
            total += i
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]