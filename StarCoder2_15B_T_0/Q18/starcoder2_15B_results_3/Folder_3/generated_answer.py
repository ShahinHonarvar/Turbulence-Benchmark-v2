def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 38 and i <= 52 and (num % -41 == 0) or num % -47 == 0))