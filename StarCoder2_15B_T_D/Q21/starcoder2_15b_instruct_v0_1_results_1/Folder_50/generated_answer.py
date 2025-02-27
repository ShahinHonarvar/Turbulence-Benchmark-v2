def all_ints_div_by_num(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 28 == 0 and 36 <= i <= 46:
            result.append(nums[i])
    return result