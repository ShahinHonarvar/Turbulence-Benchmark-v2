def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 48 and i <= 59 and (num % 88 == 0) and (num % 58 == 0)]