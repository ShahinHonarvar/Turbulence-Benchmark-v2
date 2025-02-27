def return_binary_or_hexa(tup):
    a = tup[29] + 1
    b = tup[53] - 1
    total = sum(range(a, b + 1)) - sum(tup[29:53])
    if total and total % 2 == 0:
        return '{:x}'.format(total)
    elif total:
        return '{:b}'.format(total)
    return ''