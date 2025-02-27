def return_binary_or_hexa(numbers: tuple) -> str:
    a = numbers[0]
    b = numbers[6]
    expected_range = set(range(a + 1, b))
    actual_range = set(numbers[1:7])
    missing_numbers = expected_range - actual_range
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()