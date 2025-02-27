def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 56 and i <= 88 and (num % -59 == 0) or num % -79 == 0))