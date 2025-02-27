def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums, start=1) if 1 <= i <= 4 and num % 4 == 0 and (num % -6 == 0)]