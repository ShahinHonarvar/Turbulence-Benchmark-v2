def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i in range(4, 7) and num % -6 != 0]