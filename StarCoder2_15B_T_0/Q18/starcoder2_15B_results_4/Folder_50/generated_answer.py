def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 46 and i <= 91 and (num % 67 == 0) or num % 15 == 0))