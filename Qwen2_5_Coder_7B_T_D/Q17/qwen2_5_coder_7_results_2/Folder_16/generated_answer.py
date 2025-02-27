def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums, start=1) if i >= 55 and i <= 80 and (num % 22 == 0) and (num % 32 == 0)]