def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[240:902]) if n % 546 == 0 or n % 709 == 0))