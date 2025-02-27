def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 20 and i < 35 and (nums[i] % -36 != 0):
            result.append(nums[i])
    return result