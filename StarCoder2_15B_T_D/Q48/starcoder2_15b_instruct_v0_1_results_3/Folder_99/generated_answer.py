def return_binary_or_hexa(numbers: tuple) -> str:
    a = numbers[427]
    b = numbers[669]
    expected_range = set(range(a + 1, b))
    actual_range = set(numbers[428:669])
    missing_numbers = expected_range - actual_range
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()