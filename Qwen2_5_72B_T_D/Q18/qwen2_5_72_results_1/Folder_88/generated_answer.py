def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 3 <= i <= 9 and (num % 6 == 0 or num % 1 == 0)))