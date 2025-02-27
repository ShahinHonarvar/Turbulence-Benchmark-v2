def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums) if i >= 32 and i <= 99 and (x % -11 == 0 or x % -15 == 0)))