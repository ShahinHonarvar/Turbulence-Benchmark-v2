def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 17 and i < 88 and (num % -75 != 0)]