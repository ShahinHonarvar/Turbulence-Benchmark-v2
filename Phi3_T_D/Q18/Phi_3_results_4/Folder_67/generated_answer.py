def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for i in range(24, 33):
        if nums[i] % 35 == 0 or nums[i] % 87 == 0:
            total_sum += nums[i]
    return total_sum