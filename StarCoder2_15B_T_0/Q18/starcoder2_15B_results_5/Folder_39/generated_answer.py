def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 13 and i <= 76 and (num % -66 == 0) or num % -32 == 0))