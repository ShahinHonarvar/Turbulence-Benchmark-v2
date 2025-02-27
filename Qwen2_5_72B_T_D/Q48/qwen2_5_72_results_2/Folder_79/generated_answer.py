def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[7]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[2:7]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [((0, 1, 3, 5, 6, 7, 8, 10), '11'), ((0, 2, 3, 4, 5, 6, 7, 9), 'f'), ((0, 1, 2, 3, 4, 5, 6, 7), '')]
    for nums, expected in test_cases:
        assert return_binary_or_hexa(nums) == expected, f'Failed for input: {nums}'
    print('All test cases passed.')