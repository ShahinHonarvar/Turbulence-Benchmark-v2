def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 1 and (nums[i] % 6 == 0 or nums[i] % 4 == 0):
            sum_of_ints += nums[i]
    return sum_of_ints