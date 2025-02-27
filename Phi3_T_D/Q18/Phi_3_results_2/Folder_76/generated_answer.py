def sum_ints_div_by_either_nums(nums):
    total = sum((num for num in nums[250:630] if num % 850 == 0 or num % 587 == 0))
    return total