def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 34 and i <= 69 and (num % 19 == 0) or num % 32 == 0))