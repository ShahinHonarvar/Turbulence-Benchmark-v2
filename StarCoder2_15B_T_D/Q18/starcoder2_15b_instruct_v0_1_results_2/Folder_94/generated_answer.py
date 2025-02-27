def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 93 and i <= 94 and (num % -53 == 0) or num % -91 == 0))