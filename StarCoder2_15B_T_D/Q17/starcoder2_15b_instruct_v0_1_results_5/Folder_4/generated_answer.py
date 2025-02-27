def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(86, 91):
        if nums[i] % -71 == 0 and nums[i] % -67 == 0:
            result.append(nums[i])
    return result