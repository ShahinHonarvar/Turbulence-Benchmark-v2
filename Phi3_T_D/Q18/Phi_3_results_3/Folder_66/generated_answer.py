def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[58:82], start=58) if num % 55 == 0 or num % 10 == 0))