def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for i in range(38, 82):
        if nums[i] % -61 == 0 or nums[i] % -71 == 0:
            sum_ints += nums[i]
    return sum_ints