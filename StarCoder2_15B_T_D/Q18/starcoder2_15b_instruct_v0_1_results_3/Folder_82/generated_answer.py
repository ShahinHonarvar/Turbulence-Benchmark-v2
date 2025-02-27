def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i in range(20, 201):
        if nums[i] % -20 == 0 or nums[i] % -200 == 0:
            sum_of_ints += nums[i]
    return sum_of_ints