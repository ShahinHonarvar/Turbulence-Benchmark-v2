def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[13:36]))
    if missing_sum % 2 == 0:
        return '{:x}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)