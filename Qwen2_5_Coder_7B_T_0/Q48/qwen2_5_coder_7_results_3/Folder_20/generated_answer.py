def return_binary_or_hexa(t):
    a = t[27]
    b = t[96]
    s = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[27:97]]
    if sum(missing) % 2 == 1:
        return bin(sum(missing))[2:]
    else:
        return hex(sum(missing))[2:].upper()