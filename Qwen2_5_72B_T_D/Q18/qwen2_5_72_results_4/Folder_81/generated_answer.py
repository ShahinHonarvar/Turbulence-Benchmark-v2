def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[10:101], start=10) if num % 10 == 0 or num % 100 == 0))