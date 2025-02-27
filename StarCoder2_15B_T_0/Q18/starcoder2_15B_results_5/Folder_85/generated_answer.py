def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 1 and i <= 8 and (num % -9 == 0) or num % -3 == 0))