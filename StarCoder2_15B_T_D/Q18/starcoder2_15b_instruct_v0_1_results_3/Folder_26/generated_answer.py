def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for i in range(69, 71):
        if nums[i] % 72 == 0 or nums[i] % 70 == 0:
            sum_divisible += nums[i]
    return sum_divisible