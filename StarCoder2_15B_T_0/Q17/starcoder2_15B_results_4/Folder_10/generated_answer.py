def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 32 and i <= 99 and (num % -11 == 0) and (num % -15 == 0)]