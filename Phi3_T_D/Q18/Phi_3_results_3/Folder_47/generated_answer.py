def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 42 <= i <= 87 and (num % -90 == 0 or num % -74 == 0)))