def return_binary_or_hexa(nums):
    a = nums[7]
    b = nums[9]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[8:9]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    test_cases = [((1, 2, 3, 4, 5, 6, 7, 8, 10, 12), '0f'), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), ''), ((10, 11, 12, 13, 14, 15, 16, 17, 19, 22), '111')]
    for nums, expected in test_cases:
        assert return_binary_or_hexa(nums) == expected, f'Failed for {nums}'