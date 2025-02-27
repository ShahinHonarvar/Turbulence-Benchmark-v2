def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i in range(78, 82) and num % 76 == 0 or num % 60 == 0))