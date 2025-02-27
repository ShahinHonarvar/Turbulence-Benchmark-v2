def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 31 and i <= 50 and (num % 81 == 0) and (num % 64 == 0)]