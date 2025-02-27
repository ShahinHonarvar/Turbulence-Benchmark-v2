def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums) if i >= 13 and i <= 91 and (n % -65 == 0 or n % -62 == 0)))