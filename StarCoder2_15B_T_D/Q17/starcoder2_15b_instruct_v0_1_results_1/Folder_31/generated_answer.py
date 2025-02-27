def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(56, 89):
        if nums[i] % -59 == 0 and nums[i] % -79 == 0:
            result.append(nums[i])
    return result