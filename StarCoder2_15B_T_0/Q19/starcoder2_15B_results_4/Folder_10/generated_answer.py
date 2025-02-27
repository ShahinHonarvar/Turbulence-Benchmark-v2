def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 86 and i < 89 and (num % -61 != 0)]