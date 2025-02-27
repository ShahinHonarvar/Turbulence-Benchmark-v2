def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 33 and i < 78 and (num % -17 != 0)]