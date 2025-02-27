def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 15 and i < 57 and (num % 86 != 0)]