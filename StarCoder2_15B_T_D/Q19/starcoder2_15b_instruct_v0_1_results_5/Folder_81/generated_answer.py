def all_ints_not_div_by_num(nums):
    result = []
    for i in range(10, 100):
        if nums[i] % 100 != 0:
            result.append(nums[i])
    return result