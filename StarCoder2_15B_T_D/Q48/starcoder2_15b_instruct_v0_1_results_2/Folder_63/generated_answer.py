def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    s = set(t[81:87])
    result = sum((i for i in range(a + 1, b) if i not in s))
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:].upper()