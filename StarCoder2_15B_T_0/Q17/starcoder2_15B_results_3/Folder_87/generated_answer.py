def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 18 and i <= 52 and (num % 15 == 0) and (num % 57 == 0)]