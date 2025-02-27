def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[56:89]) if num % -59 == 0 or num % -79 == 0))