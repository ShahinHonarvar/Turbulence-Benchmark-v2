def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 34 and i <= 81 and (num % 27 == 0) or num % 57 == 0))