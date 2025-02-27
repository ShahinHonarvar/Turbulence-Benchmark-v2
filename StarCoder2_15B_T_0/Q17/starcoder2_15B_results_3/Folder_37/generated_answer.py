def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 2 and i <= 7 and (num % -1 == 0) and (num % -7 == 0)]