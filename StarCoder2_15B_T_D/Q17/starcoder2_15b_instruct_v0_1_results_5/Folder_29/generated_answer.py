def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(55, 85):
        if nums[i] % -24 == 0 and nums[i] % -11 == 0:
            result.append(nums[i])
    return result