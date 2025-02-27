def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for i in range(55, 67):
        num = nums[i]
        if num % 22 == 0 or num % 82 == 0:
            sum_ints += num
    return sum_ints