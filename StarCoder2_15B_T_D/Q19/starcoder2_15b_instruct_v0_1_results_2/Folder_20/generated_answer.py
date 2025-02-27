def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 64 and i < 80 and (nums[i] % -95 != 0):
            result.append(nums[i])
    return result