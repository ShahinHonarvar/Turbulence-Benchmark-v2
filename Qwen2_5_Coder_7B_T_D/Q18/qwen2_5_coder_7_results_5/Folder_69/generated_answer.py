def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if (i >= 61 and i <= 88) and (num % 31 == 0 or num % 11 == 0)))