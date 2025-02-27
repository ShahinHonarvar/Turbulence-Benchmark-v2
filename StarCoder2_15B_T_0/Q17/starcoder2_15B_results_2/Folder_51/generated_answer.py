def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 6 and i <= 9 and (num % -1 == 0) and (num % -10 == 0)]