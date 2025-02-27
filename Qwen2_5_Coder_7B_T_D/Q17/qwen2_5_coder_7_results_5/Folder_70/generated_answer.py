def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(42, 44):
        if nums[i] % 15 == 0 and nums[i] % 87 == 0:
            result.append(nums[i])
    return result