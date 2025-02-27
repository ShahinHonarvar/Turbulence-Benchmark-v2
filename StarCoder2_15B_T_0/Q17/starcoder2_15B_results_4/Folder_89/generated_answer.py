def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 28 and i <= 96 and (num % 90 == 0) and (num % 97 == 0)]