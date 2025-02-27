def sum_ints_div_by_either_nums(nums):
    return sum((nums[55:67] if nums[55:67] else [0] for num in nums[55:67] if num % 22 == 0 or num % 82 == 0))