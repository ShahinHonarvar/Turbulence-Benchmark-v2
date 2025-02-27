def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[52]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((num for i, num in enumerate(numbers) if 38 < i < 52 and a < num < b))
    diff = expected_sum - actual_sum
    if diff % 2:
        return bin(diff)[2:]
    elif diff:
        return hex(diff)[2:]
    else:
        return ''