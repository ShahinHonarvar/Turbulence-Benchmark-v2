def all_ints_div_by_num(nums):
    result = []
    for i in range(87, 90):
        if nums[i] % 55 == 0:
            result.append(nums[i])
    return result