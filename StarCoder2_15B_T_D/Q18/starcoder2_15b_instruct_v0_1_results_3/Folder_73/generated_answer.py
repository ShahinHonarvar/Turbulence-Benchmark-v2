def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 81 and i <= 86 and (num % -33 == 0) or num % -62 == 0))