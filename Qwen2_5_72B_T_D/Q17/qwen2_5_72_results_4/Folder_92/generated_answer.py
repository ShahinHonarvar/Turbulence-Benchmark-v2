def all_ints_div_by_both_two_nums(nums):
    result = []
    if 0 <= 0 < len(nums):
        if nums[0] % 1 == 0 and nums[0] % -1 == 0:
            result.append(nums[0])
    return result