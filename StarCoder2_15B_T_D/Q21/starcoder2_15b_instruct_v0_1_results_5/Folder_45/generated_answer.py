def all_ints_div_by_num(nums):
    result = []
    for i in range(3):
        if nums[i] % 9 == 0:
            result.append(nums[i])
    return result