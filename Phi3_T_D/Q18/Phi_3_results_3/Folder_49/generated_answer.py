def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for i in range(80, 201):
        if nums[i] % 10 == 0 or nums[i] % 1000 == 0:
            total_sum += nums[i]
    return total_sum