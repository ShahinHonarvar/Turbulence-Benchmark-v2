def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[99]
    not_in_tuple = range(a + 1, b)
    total = sum((i for i in not_in_tuple if i not in tup[86:99]))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]