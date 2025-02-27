def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[20:36]) if num % -36 == 0 or num % -89 == 0))