def return_binary_or_hexa(t):
    a = t[10]
    b = t[97]
    s = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[10:98]]
    if sum(missing) % 2 == 1:
        return bin(sum(missing))[2:]
    else:
        return hex(sum(missing))[2:].upper()