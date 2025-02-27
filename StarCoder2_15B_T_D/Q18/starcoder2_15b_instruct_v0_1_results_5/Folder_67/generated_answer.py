def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 24 and i <= 32 and (num % 35 == 0) or num % 87 == 0))