def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[55:85]) if num % -24 == 0 or num % -11 == 0))