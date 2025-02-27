def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for i in range(len(nums)):
        if i >= 73 and i <= 86 and (nums[i] % 54 == 0 or nums[i] % 82 == 0):
            sum_divisible += nums[i]
    return sum_divisible