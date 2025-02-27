def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums) if i >= 18 and i <= 52 and (n % 15 == 0 or n % 57 == 0)))