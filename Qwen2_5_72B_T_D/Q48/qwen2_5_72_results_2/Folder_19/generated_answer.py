def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[2:4]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_cases = [((1, 3, 5, 7, 9), '0'), ((0, 2, 3, 4, 6), '15'), ((10, 12, 15, 19, 20), '33'), ((0, 1, 2, 3, 4), '')]
    for nums, expected in test_cases:
        assert return_binary_or_hexa(nums) == expected, f'Failed for {nums}. Expected {expected}'
    print('All test cases passed.')