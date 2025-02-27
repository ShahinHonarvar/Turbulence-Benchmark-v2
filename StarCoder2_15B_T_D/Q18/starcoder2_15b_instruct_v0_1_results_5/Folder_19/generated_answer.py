def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 1 and i <= 4 and (num % 4 == 0) or num % -6 == 0))