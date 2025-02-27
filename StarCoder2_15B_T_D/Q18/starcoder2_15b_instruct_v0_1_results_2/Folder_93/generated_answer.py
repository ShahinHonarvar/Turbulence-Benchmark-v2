def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i in range(86, 90):
        if nums[i] % -61 == 0 or nums[i] % -79 == 0:
            sum_of_ints += nums[i]
    return sum_of_ints