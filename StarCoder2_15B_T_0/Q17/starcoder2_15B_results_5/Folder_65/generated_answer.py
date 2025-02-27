def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 50 and i <= 92 and (num % -94 == 0) and (num % -95 == 0)]