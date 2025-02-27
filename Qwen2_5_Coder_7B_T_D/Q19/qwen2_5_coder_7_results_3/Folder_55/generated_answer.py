def all_ints_not_div_by_num(nums):
    return [n for i, n in enumerate(nums) if i > 0 and i < 10 and (n % 10 != 0)]