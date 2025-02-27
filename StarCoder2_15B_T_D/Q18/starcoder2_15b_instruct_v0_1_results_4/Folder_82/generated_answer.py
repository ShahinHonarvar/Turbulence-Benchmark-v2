def sum_ints_div_by_either_nums(nums):
    sum_div_by_either = 0
    for num in nums[20:201]:
        if num % -20 == 0 or num % -200 == 0:
            sum_div_by_either += num
    return sum_div_by_either