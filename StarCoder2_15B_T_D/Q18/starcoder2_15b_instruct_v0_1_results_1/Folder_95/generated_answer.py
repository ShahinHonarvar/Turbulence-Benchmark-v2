def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for i in range(57, 85):
        if nums[i] % -30 == 0 or nums[i] % -88 == 0:
            sum_divisible += nums[i]
    return sum_divisible