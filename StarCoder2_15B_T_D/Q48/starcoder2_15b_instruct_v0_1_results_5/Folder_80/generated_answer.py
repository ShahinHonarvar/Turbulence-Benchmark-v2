def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    expected_range = set(range(a + 1, b))
    actual_range = set(t[58:84])
    missing_integers = expected_range - actual_range
    sum_missing_integers = sum(missing_integers)
    if sum_missing_integers % 2 == 1:
        return bin(sum_missing_integers)[2:]
    else:
        return hex(sum_missing_integers)[2:].upper()