def all_ints_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 0 and i <= 2 and (nums[i] % -8 == 0):
            result.append(nums[i])
    return result