def return_binary_or_hexa(t: tuple) -> str:
    a = t[10]
    b = t[97]
    s = sum((i for i in range(a + 1, b) if i not in t))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].lower()