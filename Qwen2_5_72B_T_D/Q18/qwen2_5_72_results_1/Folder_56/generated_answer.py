def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(7, 10):
        if nums[i] % -9 == 0 or nums[i] % -7 == 0:
            sum_nums += nums[i]
    return sum_nums