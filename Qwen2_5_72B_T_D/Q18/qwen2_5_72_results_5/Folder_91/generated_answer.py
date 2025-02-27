def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[:5]) if n % 8 == 0 or n % -3 == 0))