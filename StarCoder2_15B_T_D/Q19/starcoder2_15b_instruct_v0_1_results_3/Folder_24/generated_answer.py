def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 41 and i < 69 and (num % -82 != 0)]