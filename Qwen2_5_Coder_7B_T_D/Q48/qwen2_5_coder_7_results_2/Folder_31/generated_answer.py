def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    s = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[a + 1:b]]
    if missing == list(range(a + 1, b)):
        return ''
    elif sum(missing) % 2 == 1:
        return bin(sum(missing))[2:]
    else:
        return hex(sum(missing))[2:].upper()