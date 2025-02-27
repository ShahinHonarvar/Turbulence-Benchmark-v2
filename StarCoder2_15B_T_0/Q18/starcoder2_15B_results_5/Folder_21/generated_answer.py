def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 315 and i <= 934 and (num % -897 == 0) or num % -556 == 0))