def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 154 and i <= 798 and (num % 275 == 0) or num % 580 == 0))