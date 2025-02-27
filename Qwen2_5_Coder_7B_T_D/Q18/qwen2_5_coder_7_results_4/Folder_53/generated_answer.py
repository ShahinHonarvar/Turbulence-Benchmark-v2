def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[200:201] if n % 17 == 0 or n % -5 == 0))