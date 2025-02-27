def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[68:100]) if num % -37 == 0 or num % -26 == 0))