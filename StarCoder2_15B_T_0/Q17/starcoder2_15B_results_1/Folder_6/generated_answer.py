def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 41 and i <= 56 and (num % 82 == 0) and (num % 90 == 0)]