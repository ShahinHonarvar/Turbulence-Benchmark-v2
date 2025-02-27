def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[200]
    expected_numbers = set(range(a + 1, b))
    actual_numbers = set(numbers[a + 1:b])
    missing_numbers = expected_numbers - actual_numbers
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:].rstrip('L')
    return bin(sum_of_missing_numbers)[2:]