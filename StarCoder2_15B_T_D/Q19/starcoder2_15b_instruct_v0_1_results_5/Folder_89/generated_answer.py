def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 48 and i < 62 and (nums[i] % 28 != 0):
            result.append(nums[i])
    return result