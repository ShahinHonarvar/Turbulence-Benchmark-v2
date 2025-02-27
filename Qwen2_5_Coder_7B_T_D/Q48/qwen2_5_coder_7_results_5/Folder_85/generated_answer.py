def return_binary_or_hexa(tup):
    a, b = (tup[1], tup[8])
    total = sum(range(a + 1, b))
    missing = sum((x for x in range(a + 1, b) if x not in tup[1:9]))
    if total == missing:
        return ''
    elif (missing + total) % 2 == 0:
        return hex(missing + total)[2:].upper()
    else:
        return bin(missing + total)[2:]