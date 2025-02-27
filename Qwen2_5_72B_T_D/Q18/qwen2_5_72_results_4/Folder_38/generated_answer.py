def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[10:77], start=10) if num % -40 == 0 or num % -12 == 0))