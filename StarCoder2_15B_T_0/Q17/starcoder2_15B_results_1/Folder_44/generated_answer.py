def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 25 and i <= 70 and (num % 74 == 0) and (num % 15 == 0)]