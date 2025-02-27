def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 13 and i < 70 and (num % -78 != 0)]