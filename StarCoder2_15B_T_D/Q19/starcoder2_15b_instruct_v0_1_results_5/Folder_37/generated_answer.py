def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 1 and i < len(nums) - 1 and (num % 5 != 0)]