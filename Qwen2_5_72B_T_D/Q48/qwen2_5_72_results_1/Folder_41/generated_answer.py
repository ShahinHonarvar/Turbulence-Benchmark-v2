def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[8]
    present_nums = set(nums[4:8])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_nums))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    test_cases = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'b'), ([1, 2, 3, 4, 6, 8, 10, 11, 12, 13, 14], '1f'), ([1, 2, 3, 4, 5, 7, 8, 9, 10, 14, 15], '1c'), ([1, 2, 3, 6, 7, 8, 9, 10, 14, 15, 16], '')]
    for nums, expected in test_cases:
        assert return_binary_or_hexa(nums) == expected, f'Failed for {nums}'
    print('All test cases passed.')