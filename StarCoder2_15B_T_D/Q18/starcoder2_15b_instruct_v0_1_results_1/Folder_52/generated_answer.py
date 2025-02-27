def sum_ints_div_by_either_nums(nums):
    sum_div_by_either = 0
    for i in range(48, 60):
        if nums[i] % 88 == 0 or nums[i] % 58 == 0:
            sum_div_by_either += nums[i]
    return sum_div_by_either