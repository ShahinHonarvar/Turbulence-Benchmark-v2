def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[1:6]]
    if sum(missing) == total:
        return ''
    elif sum(missing) % 2 == 0:
        return hex(sum(missing))[2:].upper()
    else:
        return bin(sum(missing))[2:]