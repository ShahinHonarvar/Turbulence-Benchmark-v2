def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[91]
    expected_range = set(range(a + 1, b))
    actual_range = set(tup[45:91])
    missing_numbers = expected_range - actual_range
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 0:
        result = hex(sum_of_missing_numbers)[2:]
    else:
        result = bin(sum_of_missing_numbers)[2:]
    return result