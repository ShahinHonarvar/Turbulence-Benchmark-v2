def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[36:86]) if num % -27 == 0 or num % -96 == 0))