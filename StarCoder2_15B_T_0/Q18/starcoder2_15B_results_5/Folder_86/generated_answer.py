def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 54 and i <= 79 and (num % 54 == 0 or num % 28 == 0)))