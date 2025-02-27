def return_binary_or_hexa(mixed_tuple):
    a, b = (mixed_tuple[3], mixed_tuple[8])
    sum = sum((x for x in range(a + 1, b) if x not in mixed_tuple[:9:3]))
    if sum % 2 == 0:
        return '{:X}'.format(sum)
    else:
        return '{:b}'.format(sum)