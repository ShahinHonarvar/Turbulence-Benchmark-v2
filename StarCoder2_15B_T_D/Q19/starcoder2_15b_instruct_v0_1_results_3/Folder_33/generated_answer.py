def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 103 and i < 574 and (num % -514 != 0)]