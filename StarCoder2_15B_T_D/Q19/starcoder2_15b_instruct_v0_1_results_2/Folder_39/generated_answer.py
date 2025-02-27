def all_ints_not_div_by_num(nums):
    result = []
    for i in range(22, 97):
        if nums[i] % -46 != 0:
            result.append(nums[i])
    return result