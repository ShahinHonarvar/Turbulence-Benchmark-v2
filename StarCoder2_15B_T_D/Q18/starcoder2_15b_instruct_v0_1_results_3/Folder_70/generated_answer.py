def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i in range(42, 44):
        if nums[i] % 15 == 0 or nums[i] % 87 == 0:
            sum_of_ints += nums[i]
    return sum_of_ints