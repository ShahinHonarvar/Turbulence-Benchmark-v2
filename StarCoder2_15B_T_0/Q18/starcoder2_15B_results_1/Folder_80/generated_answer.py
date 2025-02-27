def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 14 and i <= 93 and (num % 71 == 0) or num % 81 == 0))