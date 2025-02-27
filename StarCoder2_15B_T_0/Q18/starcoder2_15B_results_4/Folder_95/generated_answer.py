def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 57 and i <= 84 and (num % -30 == 0) or num % -88 == 0))