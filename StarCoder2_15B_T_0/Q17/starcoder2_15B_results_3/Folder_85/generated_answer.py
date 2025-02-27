def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 1 and i <= 8 and (num % -9 == 0) and (num % -3 == 0)]