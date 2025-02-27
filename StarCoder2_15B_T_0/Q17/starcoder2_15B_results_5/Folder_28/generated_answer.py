def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 34 and i <= 81 and (num % 27 == 0) and (num % 57 == 0)]