def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if 7 < i < 9 and num % -9 != 0]