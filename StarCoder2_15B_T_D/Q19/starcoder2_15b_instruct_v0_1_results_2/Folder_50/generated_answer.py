def all_ints_not_div_by_num(nums):
    return [n for i, n in enumerate(nums) if i >= 13 and i < 76 and (n % 44 != 0)]