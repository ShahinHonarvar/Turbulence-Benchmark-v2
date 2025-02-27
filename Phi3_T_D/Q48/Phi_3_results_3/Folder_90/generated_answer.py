def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[90]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[60:91]))
    if missing_sum:
        return bin(missing_sum)[2:] if missing_sum % 2 else '{:x}'.format(missing_sum)
    return ''