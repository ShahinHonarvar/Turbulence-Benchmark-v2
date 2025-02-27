def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums) if i >= 29 and i <= 53 and (n % -68 == 0) or n % -85 == 0))