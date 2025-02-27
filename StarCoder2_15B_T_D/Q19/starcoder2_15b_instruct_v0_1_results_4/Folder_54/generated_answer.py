def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 19 and i < 94 and (num % -32 != 0)]