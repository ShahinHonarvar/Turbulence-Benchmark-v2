def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[73]
    b = tuple_of_ints[84]
    expected_range = set(range(a + 1, b))
    actual_range = set(tuple_of_ints[74:84])
    missing_numbers = expected_range - actual_range
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()