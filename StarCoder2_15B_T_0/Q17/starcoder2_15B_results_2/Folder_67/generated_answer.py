def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 24 and i <= 32 and (num % 35 == 0) and (num % 87 == 0)]