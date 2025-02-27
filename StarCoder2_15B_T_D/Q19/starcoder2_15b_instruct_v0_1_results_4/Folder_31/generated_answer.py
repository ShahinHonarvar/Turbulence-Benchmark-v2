def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 18 and i < 37 and (num % -67 != 0)]