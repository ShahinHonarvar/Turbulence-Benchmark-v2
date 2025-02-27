def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    expected_set = set(range(a + 1, b))
    actual_set = set(numbers[61:90])
    missing_numbers = expected_set - actual_set
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]