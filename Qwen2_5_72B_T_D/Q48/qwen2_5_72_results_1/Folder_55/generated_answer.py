def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[11:12]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]

def check():
    test_cases = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15], '26'), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16], ''), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13], '10')]
    for nums, expected in test_cases:
        result = return_binary_or_hexa(nums)
        assert result == expected, f'Expected {expected}, got {result}'
    print('All tests passed.')