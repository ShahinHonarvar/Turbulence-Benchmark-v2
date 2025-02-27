def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in tup[275:872]]
    if sum(missing) == total:
        return ''
    elif sum(missing) % 2 == 1:
        return bin(sum(missing))[2:]
    else:
        return hex(sum(missing))[2:].upper()