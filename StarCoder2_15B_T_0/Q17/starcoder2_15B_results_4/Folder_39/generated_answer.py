def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 13 and i <= 76 and (num % -66 == 0) and (num % -32 == 0)]