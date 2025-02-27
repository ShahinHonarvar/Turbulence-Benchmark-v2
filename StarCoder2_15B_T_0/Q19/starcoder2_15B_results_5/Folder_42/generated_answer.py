def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 11 and i < 56 and (num % 90 != 0)]