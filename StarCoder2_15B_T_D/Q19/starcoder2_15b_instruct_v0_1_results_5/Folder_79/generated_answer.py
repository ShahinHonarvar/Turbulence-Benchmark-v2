def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 8 and i < 9 and (num % -3 != 0)]