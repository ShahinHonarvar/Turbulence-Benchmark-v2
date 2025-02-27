def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 20 and i < 200 and (num % -200 != 0)]