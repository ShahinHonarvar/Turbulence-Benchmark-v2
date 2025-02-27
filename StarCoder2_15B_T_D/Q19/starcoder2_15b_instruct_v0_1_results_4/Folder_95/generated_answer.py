def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 38 and i < 52 and (num % -41 != 0)]