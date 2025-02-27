def return_binary_or_hexa(numbers):
    a = numbers[77]
    b = numbers[84]
    expected_set = set(range(a + 1, b))
    actual_set = set(numbers[78:84])
    missing_numbers = expected_set - actual_set
    total_sum = sum(missing_numbers)
    if total_sum % 2:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]