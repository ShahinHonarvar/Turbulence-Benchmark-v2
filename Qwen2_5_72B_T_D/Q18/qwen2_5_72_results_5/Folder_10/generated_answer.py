def sum_ints_div_by_either_nums(nums):
    return sum((num for idx, num in enumerate(nums[32:100], start=32) if idx >= 32 and (num % -11 == 0 or num % -15 == 0)))