def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[14:35]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_cases = [([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], '1011011110'), ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44], '1b8'), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], '')]
    for nums, expected in test_cases:
        result = return_binary_or_hexa(nums)
        assert result == expected, f'Failed for {nums}. Expected {expected}, got {result}.'
    print('All test cases passed.')