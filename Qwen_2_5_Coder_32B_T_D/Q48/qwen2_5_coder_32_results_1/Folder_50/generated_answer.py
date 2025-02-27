def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    total_sum = 0
    expected_set = set(range(a + 1, b))
    given_set = set(numbers[14:76])
    missing_numbers = expected_set - given_set
    for number in missing_numbers:
        total_sum += number
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]