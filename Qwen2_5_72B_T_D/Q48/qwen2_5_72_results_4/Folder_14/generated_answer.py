def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[5]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[3:5]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((1, 3, 4, 5, 6, 8, 10, 15), '111'), ((0, 2, 3, 4, 5, 7, 12, 20), '9'), ((0, 1, 2, 3, 4, 5, 6, 10), '')]
    for nums, expected in test_cases:
        result = return_binary_or_hexa(nums)
        assert result == expected, f'Expected {expected}, got {result}'
    print('All test cases passed.')