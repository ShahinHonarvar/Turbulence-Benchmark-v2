def all_ints_not_div_by_num(nums):
    return [num for idx, num in enumerate(nums) if idx > 14 and idx < 21 and (num % -93 != 0)]