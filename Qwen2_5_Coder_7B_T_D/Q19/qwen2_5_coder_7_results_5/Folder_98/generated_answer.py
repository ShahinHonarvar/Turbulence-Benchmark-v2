def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i > 0 and i < 5 and (num % 13 != 0)]