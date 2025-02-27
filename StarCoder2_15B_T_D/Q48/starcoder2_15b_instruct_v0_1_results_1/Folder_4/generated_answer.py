def return_binary_or_hexa(tup):
    a = tup[49]
    b = tup[74]
    expected_range = set(range(a + 1, b))
    actual_range = set(tup[49:75])
    missing_integers = expected_range - actual_range
    sum_of_missing_integers = sum(missing_integers)
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:]