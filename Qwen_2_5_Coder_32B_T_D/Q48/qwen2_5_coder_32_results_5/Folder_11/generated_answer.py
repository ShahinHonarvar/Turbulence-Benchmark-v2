def return_binary_or_hexa(numbers):
    a = numbers[48]
    b = numbers[76]
    expected_set = set(range(a + 1, b))
    actual_set = set(numbers[49:76])
    missing_numbers = expected_set - actual_set
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]