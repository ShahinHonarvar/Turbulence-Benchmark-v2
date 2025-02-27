def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 2 and i <= 7 and all([num % -1 == 0, num % -7 == 0])]