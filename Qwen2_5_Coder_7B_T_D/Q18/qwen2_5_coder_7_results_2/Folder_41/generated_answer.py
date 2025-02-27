def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[:10]) if i in (0, 9) and (n % 6 == 0 or n % -3 == 0)))