def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 24 and i < 32 and (num % 35 != 0)]