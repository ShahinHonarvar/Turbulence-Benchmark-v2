def return_binary_or_hexa(t):
    a, b = (t[69], t[97])
    s = sum((x for x in range(a + 1, b) if x not in t[69:98]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()