def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 2 and i < len(nums) - 2 and (num % 2 != 0)]