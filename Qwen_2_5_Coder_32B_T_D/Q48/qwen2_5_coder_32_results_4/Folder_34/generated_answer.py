def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((num for num in numbers[61:200] if a < num < b))
    missing_sum = expected_sum - actual_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]