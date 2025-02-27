def all_ints_not_div_by_num(nums, num):
    result = []
    for i in range(len(nums)):
        if i % num != 0:
            result.append(nums[i])
    return result