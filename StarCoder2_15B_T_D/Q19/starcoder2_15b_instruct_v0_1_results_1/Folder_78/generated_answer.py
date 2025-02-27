def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 10 and i < 55 and (num % 36 != 0)]