def all_ints_not_div_by_num(nums):
    return [n for i, n in enumerate(nums) if i > 70 and i < 98 and (n % -88 != 0)]