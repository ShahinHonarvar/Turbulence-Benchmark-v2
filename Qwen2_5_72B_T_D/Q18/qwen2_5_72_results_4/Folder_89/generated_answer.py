def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[28:97]) if num % 90 == 0 or num % 97 == 0))