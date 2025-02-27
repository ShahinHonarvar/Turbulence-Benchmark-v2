def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 14 and i < 21 and (num % -93 != 0)]