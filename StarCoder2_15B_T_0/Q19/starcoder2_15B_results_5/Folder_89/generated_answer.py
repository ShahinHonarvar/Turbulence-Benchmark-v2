def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 48 and i < 62 and (num % 28 != 0)]