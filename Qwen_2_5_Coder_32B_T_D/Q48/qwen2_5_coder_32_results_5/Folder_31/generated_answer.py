def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    total_sum = 0
    expected_sum = sum(range(a + 1, b))
    present_sum = sum(numbers[34:78])
    missing_sum = expected_sum - present_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]