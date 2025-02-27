def return_binary_or_hexa(tup):
    a = tup[57]
    b = tup[84]
    present = set(tup[58:84])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]