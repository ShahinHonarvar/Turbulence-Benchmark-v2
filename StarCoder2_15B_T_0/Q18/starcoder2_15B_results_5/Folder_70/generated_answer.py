def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i in range(42, 44) and num % 15 == 0 or num % 87 == 0))