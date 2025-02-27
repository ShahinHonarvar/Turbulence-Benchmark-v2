def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i < 1 or i > 1 or num % 1 != 0]