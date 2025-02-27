def sum_odd_ints_inclusive(nums):
    start_index = 262
    end_index = 746
    return sum((num for num in nums[start_index:end_index + 1] if num % 2 != 0))