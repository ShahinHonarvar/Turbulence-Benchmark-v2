def sum_ints_div_by_either_nums(nums):
    return sum((num for idx, num in enumerate(nums) if idx >= 58 and idx <= 75 and (num % 72 == 0 or num % 62 == 0)))