def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[:2]) if num % 2 == 0 or num % 1 == 0))