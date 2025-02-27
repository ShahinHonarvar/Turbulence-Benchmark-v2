def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for num in nums[86:90]:
        if num % -61 == 0 or num % -79 == 0:
            sum_of_ints += num
    return sum_of_ints