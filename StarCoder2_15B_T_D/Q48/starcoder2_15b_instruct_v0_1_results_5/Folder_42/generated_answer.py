def return_binary_or_hexa(tup):
    a = tup[18]
    b = tup[60]
    expected_range = set(range(a + 1, b))
    actual_range = set(tup[19:60])
    missing_numbers = expected_range - actual_range
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:]
    else:
        return bin(sum_of_missing_numbers)[2:]