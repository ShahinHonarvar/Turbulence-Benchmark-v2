def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 57 and i <= 85 and (num % -77 == 0) or num % -32 == 0))