def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 15 and i < 92 and (num % 59 != 0)]