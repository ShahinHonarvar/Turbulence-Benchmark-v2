def sum_ints_div_by_either_nums(nums):
    divisible_sum = sum((num for num in nums[299:383] if num % 858 == 0 or num % 952 == 0))
    return divisible_sum