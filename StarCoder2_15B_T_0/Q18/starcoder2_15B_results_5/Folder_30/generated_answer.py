def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 11 and i <= 76 and (num % -81 == 0) or num % -94 == 0))