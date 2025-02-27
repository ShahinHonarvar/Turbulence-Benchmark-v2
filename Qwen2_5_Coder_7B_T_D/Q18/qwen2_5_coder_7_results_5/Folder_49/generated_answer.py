def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 80 <= i <= 200 and (num % 10 == 0 or num % 1000 == 0)))