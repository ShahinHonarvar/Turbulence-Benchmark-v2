def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 0 and i <= 9 and (num % 6 == 0) or num % -3 == 0))