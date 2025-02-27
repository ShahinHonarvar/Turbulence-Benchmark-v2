def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i > 45 and i < 72 and (num % 93 != 0)]