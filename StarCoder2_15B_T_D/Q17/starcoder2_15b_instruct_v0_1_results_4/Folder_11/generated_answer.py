def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(22, 25):
        if nums[i] % -85 == 0 and nums[i] % -30 == 0:
            result.append(nums[i])
    return result