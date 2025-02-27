def all_ints_div_by_both_two_nums(nums):
    return [n for i, n in enumerate(nums) if i >= 55 and i <= 80 and (n % 22 == 0) and (n % 32 == 0)]