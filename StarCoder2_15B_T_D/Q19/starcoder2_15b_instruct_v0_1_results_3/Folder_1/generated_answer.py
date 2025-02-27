def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 21 and i < 69 and (num % -69 != 0)]