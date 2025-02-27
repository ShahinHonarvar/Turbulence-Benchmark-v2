def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums, start=1) if 1 <= i <= 8 and (n % -9 == 0 or n % -3 == 0)))