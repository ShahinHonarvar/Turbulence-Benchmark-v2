def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 15 and i < 63 and (num % 34 != 0)]