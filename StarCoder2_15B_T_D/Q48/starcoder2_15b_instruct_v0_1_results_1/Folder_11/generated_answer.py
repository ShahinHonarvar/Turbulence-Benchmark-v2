def return_binary_or_hexa(t: tuple) -> str:
    a = t[48]
    b = t[76]
    s = sum(range(a + 1, b))
    if s % 2 == 1:
        return bin(s)[2:]
    return hex(s)[2:]