def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 31 and i < 69 and (num % -70 != 0)]