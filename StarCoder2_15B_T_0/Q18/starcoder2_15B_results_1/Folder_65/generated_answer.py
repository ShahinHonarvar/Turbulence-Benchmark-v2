def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 50 and i <= 92 and (num % -94 == 0) or num % -95 == 0))