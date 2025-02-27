def all_ints_div_by_both_two_nums(nums):
    result = [num for i, num in enumerate(nums) if i >= 72 and i <= 93 and (num % 32 == 0) and (num % 44 == 0)]
    return result