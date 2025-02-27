def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 55 and i <= 84 and (num % -24 == 0) or num % -11 == 0))