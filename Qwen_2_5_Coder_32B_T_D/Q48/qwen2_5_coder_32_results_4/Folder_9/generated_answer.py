def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    total_sum = 0
    expected_set = set(range(a + 1, b))
    given_set = set(numbers[71:200])
    missing_numbers = expected_set - given_set
    for num in missing_numbers:
        total_sum += num
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]