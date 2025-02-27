def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 18 and i <= 52 and (num % 15 == 0 or num % 57 == 0)))