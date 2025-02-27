def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 0 and i <= 4 and (num % 8 == 0) and (num % -3 == 0)]