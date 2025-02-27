def sum_ints_div_by_either_nums(nums):
    sum_val = 0
    for i in range(5):
        if nums[i] % 8 == 0 or nums[i] % -3 == 0:
            sum_val += nums[i]
    return sum_val