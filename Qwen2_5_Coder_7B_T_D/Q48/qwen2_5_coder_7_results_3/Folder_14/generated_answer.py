def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[5]
    total = sum(range(a + 1, b))
    missing = [x for x in range(a + 1, b) if x not in tup[2:6]]
    total += sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()