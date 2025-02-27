def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for i in range(61, 89):
        if nums[i] % 31 == 0 or nums[i] % 11 == 0:
            sum_divisible += nums[i]
    return sum_divisible