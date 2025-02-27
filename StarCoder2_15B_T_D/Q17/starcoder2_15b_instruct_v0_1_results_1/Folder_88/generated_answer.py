def all_ints_div_by_both_two_nums(nums):
    return [num for idx, num in enumerate(nums) if idx >= 3 and idx <= 9 and (num % 6 == 0) and (num % 1 == 0)]