def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 64 and i < 80 and (num % -95 != 0)]