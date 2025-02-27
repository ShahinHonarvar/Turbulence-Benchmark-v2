def sum_odd_ints_inclusive(nums):
    start_index, end_index = (29, 79)
    total_sum = sum((num for num in nums[start_index:end_index + 1] if num % 2 != 0))
    return total_sum