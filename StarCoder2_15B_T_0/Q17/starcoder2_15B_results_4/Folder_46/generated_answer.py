def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 11 and i <= 46 and (num % 55 == 0) and (num % 36 == 0)]