def all_ints_div_by_num(nums):
    result = []
    if len(nums) >= 93:
        for i in range(86, 93):
            if nums[i] % 86 == 0:
                result.append(nums[i])
    return result