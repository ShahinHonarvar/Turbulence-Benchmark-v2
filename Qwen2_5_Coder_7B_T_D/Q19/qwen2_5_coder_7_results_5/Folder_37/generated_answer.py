def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if 1 < i < 3 and num % 5 != 0]