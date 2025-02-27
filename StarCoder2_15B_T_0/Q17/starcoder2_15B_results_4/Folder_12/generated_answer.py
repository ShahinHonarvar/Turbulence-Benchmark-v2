def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 35 and i <= 64 and (num % -30 == 0) and (num % -95 == 0)]