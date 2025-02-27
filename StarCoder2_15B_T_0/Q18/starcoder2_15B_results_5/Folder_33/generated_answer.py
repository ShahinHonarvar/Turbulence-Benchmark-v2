def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i in range(281, 695):
        if nums[i] % -722 == 0 or nums[i] % -731 == 0:
            sum_of_ints += nums[i]
    return sum_of_ints