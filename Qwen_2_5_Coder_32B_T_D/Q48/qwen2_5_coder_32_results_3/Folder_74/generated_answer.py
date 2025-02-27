def return_binary_or_hexa(t):
    a, b = (t[69], t[97])
    s = 0
    for i in range(a + 1, b):
        if i not in t[69:98]:
            s += i
    if not s:
        return ''
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:].upper()