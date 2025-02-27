def all_ints_div_by_num(nums):
    return [n for i, n in enumerate(nums) if i >= 10 and i <= 52 and (n % -12 == 0)]