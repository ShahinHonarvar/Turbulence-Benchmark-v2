def all_ints_not_div_by_num(nums):
    result = []
    for i in range(46, 91):
        if nums[i] % 67 != 0:
            result.append(nums[i])
    return result