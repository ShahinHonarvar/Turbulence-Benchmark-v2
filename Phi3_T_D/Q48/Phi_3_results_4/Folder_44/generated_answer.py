def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    total = sum((i for i in range(a + 1, b) if i not in t[36:53]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]