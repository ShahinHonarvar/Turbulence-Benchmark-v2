def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 29 and i <= 45 and (num % 27 == 0) or num % 81 == 0))