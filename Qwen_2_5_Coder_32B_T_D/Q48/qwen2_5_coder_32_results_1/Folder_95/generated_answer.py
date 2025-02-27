def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    total_sum = 0
    expected_set = set(range(a + 1, b))
    present_set = set(numbers[33:99])
    missing_numbers = expected_set - present_set
    for number in missing_numbers:
        total_sum += number
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]