def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 36 and i <= 85 and (num % -27 == 0) and (num % -96 == 0)]