def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i in range(1, 2) and num % 8 != 0]