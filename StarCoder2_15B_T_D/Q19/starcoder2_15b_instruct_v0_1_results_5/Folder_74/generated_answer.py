def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 93 and i < 94 and (nums[i] % 57 != 0):
            result.append(nums[i])
    return result