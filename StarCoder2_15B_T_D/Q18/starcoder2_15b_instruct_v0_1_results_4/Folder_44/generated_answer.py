def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums) if i >= 25 and i <= 70 and (n % 74 == 0) or n % 15 == 0))