def sum_ints_div_by_either_nums(nums):
    return sum((val for val in nums[:5] if val % 8 == 0 or val % -3 == 0))