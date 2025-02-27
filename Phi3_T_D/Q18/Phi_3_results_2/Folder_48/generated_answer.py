def sum_ints_div_by_either_nums(nums):
    sum_divisible = sum((n for n in nums[306:958] if n % 982 == 0 or n % 319 == 0))
    return sum_divisible