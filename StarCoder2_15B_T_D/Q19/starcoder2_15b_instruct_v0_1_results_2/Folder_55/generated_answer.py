def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 0 and i < 9 and (nums[i] % 10 != 0):
            result.append(nums[i])
    return result