def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 18 and i < 60 and (num % 86 != 0)]