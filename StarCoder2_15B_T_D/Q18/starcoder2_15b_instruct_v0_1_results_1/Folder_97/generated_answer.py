def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 58 and i <= 75 and (num % 72 == 0 or num % 62 == 0)))