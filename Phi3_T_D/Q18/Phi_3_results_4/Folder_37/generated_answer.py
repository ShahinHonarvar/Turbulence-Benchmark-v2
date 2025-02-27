def sum_ints_div_by_either_nums(nums):
    sum_result = sum((num for i, num in enumerate(nums[2:8], start=2) if num % -1 == 0 or num % -7 == 0))
    return sum_result