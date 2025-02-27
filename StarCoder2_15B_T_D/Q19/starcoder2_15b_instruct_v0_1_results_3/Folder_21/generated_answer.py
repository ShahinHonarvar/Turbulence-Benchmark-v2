def all_ints_not_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if i >= 469 and i < 566 and (nums[i] % -692 != 0):
            result.append(nums[i])
    return result