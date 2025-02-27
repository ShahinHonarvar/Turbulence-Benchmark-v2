def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 10 and i <= 28 and (num % -61 == 0) or num % -64 == 0))