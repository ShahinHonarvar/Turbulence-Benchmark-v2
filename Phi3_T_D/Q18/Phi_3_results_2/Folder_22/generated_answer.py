def sum_ints_div_by_either_nums(nums):
    total = sum((x for i, x in enumerate(nums) if 40 <= i <= 200 and (x % 21 == 0 or x % 71 == 0)))
    return total