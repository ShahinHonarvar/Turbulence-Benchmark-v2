def sum_ints_div_by_either_nums(nums):
    sum_div_by_either = 0
    for i in range(len(nums)):
        if i >= 154 and i <= 798 and (nums[i] % 275 == 0 or nums[i] % 580 == 0):
            sum_div_by_either += nums[i]
    return sum_div_by_either