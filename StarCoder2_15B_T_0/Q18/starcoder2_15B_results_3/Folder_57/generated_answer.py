def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 51 and i <= 76 and (num % -90 == 0) or num % -59 == 0))