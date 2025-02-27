def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 32 and i < 44 and (num % 34 != 0)]