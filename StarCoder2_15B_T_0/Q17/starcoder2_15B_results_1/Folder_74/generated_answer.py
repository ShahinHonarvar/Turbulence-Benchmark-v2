def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 90 and i <= 97 and (num % 13 == 0) and (num % 35 == 0)]