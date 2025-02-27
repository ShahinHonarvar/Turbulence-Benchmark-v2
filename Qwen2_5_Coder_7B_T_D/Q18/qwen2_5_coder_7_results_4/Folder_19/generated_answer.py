def sum_ints_div_by_either_nums(nums):
    return sum((num for index, num in enumerate(nums, start=1) if (index >= 1 and index <= 4) and (num % 4 == 0 or num % -6 == 0)))