def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i <= 5 and num % -1 == 0 or num % 13 == 0))