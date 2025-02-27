def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i in range(299, 383):
        if nums[i] % 858 == 0 or nums[i] % 952 == 0:
            sum_of_ints += nums[i]
    return sum_of_ints