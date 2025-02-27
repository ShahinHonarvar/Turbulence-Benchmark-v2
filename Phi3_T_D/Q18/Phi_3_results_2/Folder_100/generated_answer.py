def sum_ints_div_by_either_nums(nums):
    start_index, end_index = (72, 93)
    return sum((num for i, num in enumerate(nums[start_index:end_index + 1]) if num % 32 == 0 or num % 44 == 0))