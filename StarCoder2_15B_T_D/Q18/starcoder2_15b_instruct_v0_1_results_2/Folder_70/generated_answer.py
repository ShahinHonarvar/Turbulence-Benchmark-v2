def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums) if i in range(42, 44) and x % 15 == 0 or x % 87 == 0))