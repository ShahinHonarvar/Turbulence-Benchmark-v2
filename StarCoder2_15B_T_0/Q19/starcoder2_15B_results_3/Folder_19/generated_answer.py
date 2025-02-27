def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 4 and i < 5 and (num % -7 != 0)]