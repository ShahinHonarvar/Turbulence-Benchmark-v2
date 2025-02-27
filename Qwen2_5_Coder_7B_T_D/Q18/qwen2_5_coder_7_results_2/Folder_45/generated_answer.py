def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[30:201]) if num % -115 == 0 or num % 115 == 0))