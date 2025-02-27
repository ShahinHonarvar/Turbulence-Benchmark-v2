def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 200 and (num % 17 == 0 or num % -5 == 0)))