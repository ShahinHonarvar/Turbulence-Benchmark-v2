def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 29 and i <= 45 and (num % 27 == 0) and (num % 81 == 0)]