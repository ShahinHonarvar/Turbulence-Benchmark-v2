def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 20 and i < 43 and (num % 95 != 0)]