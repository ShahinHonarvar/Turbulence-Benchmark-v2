def return_binary_or_hexa(nums):
    a = nums[50]
    b = nums[92]
    expected_range = set(range(a + 1, b))
    actual_range = set(nums[51:92])
    missing_nums = expected_range - actual_range
    if not missing_nums:
        return ''
    sum_of_missing_nums = sum(missing_nums)
    if sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:]