def return_binary_or_hexa(t):
    a, b = (t[35], t[64])
    missing = [i for i in range(a + 1, b) if i not in t[35:65]]
    total = sum(missing)
    return bin(total)[2:] if total % 2 else hex(total)[2:]