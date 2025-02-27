def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums) if 61 <= i <= 88 and (n % 31 == 0 or n % 11 == 0)))