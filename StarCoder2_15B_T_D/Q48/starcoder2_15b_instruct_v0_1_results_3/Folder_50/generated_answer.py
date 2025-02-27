def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[76]
    expected_range = set(range(a + 1, b))
    actual_range = set(tup[14:76])
    missing_integers = expected_range - actual_range
    if not missing_integers:
        return ''
    sum_missing_integers = sum(missing_integers)
    if sum_missing_integers % 2 == 1:
        return bin(sum_missing_integers)[2:]
    else:
        return hex(sum_missing_integers)[2:].upper()