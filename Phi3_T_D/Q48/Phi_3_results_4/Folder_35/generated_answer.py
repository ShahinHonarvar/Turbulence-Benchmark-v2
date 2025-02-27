def return_binary_or_hexa(tup):
    a = tup[77]
    b = tup[84]
    missing_sum = sum([i for i in range(a + 1, b) if i not in tup[77:85]])
    if missing_sum % 2 == 0:
        return '{:X}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)