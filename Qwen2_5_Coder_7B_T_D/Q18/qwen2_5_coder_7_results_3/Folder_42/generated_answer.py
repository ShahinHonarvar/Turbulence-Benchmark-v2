def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums, 29) if 29 <= i <= 45 and (x % 27 == 0 or x % 81 == 0)))