def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 199 and i < 201 and (num % -200 != 0)]