def all_ints_not_div_by_num(nums):
    result = []
    for i in range(56, 88):
        if nums[i] % -59 != 0:
            result.append(nums[i])
    return result