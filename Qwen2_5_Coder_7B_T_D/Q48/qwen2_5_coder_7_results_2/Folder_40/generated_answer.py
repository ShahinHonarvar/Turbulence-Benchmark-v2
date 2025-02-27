def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[3]
    total = sum(range(a + 1, b))
    missing = set(range(a + 1, b)) - set(tup[1:3])
    for num in missing:
        total -= num
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]