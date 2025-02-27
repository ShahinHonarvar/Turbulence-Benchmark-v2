def all_ints_not_div_by_num(nums):
    result = []
    for i in range(0, 7):
        if nums[i] % 7 != 0:
            result.append(nums[i])
    return result