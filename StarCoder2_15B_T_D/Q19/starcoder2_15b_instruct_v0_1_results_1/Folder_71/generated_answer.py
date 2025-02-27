def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 21 and i < 51 and (num % -77 != 0)]