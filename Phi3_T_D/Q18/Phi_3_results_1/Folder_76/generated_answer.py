def sum_ints_div_by_either_nums(nums):
    divisible_sum = sum((num for n in nums[250:630] if n % 850 == 0 or n % 587 == 0))
    return divisible_sum