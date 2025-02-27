def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[:7]) if num % -5 == 0 or num % -6 == 0))