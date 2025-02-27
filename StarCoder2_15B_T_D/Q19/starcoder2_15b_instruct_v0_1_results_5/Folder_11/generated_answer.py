def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 36 and i < 85 and (num % -27 != 0)]