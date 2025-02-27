def sum_even_ints_inclusive(nums):
    start_idx, end_idx = (35, 49)
    return sum((num for num in nums[start_idx:end_idx + 1] if num % 2 == 0))