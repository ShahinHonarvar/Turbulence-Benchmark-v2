def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 14 and i <= 93 and (num % 71 == 0) and (num % 81 == 0)]