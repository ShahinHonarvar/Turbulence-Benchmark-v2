def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[200]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in tup[60:201]]
    for num in missing:
        total -= num
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()