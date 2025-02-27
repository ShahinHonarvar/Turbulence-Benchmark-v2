def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums) if i >= 14 and i <= 93 and (n % 71 == 0) or n % 81 == 0))