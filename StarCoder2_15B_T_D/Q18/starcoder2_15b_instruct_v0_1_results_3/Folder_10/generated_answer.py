def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i in range(32, 100):
        if nums[i] % -11 == 0 or nums[i] % -15 == 0:
            sum_of_ints += nums[i]
    return sum_of_ints