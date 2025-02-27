def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i not in range(0, 6) or num % 13 != 0]