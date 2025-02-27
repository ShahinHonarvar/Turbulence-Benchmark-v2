def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 5 and i <= 80 and (num % 22 == 0 or num % 32 == 0)))