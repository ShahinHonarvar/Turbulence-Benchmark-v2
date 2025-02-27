def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i in {0, len(nums) - 1} and num % 1 == 0))