def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums, start=1) if 7 <= i <= 7 and (num % 5 == 0 or num % 7 == 0)))