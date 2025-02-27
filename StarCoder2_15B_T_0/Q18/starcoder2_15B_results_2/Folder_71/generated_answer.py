def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 68 and i <= 99 and (num % -37 == 0) or num % -26 == 0))