def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 22 and i < 97 and (num % -46 != 0)]