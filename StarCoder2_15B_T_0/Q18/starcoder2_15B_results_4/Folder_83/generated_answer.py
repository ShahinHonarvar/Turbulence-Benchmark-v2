def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 90 and i <= 200 and (num % -31 == 0) or num % 13 == 0))