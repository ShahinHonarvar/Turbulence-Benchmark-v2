def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 44 and i <= 59 and (num % 39 == 0 or num % 15 == 0)))