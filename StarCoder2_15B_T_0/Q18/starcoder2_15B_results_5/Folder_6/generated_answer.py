def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 41 and i <= 56 and (num % 82 == 0) or num % 90 == 0))