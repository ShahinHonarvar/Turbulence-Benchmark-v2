def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 81 and i <= 89 and (num % 56 == 0) and (num % 68 == 0)]