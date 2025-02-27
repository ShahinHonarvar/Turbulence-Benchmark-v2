def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 250 and i <= 629 and (num % 850 == 0) or num % 587 == 0))